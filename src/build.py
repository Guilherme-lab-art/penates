#!/usr/bin/env python3
"""Pénates — build single-file. template.html → ../index.html
Inline: Fraunces woff2 (4 subsets), GSAP+ST+ScrollSmoother+SplitText, fotos, brand PNGs."""
import base64, io, re, sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent      # penates-site/
SRC, ASSETS = ROOT / 'src', ROOT / 'assets'
OUT = ROOT / 'index.html'

def b64(p, mime):
    return f"data:{mime};base64," + base64.b64encode(Path(p).read_bytes()).decode()

def png_small(p):
    """PNG RGBA → palette (tinta+poucas cores) para embutir leve."""
    im = Image.open(p).convert('RGBA')
    q = im.quantize(colors=96, method=Image.FASTOCTREE)
    buf = io.BytesIO(); q.save(buf, 'PNG', optimize=True)
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()

# LISTA, não set: iteração de set com strings é randomizada por processo
# (PYTHONHASHSEED) e embaralhava a ordem dos @font-face a cada build.
# Ordem = italic primeiro, igual ao que está no live v7 (diff mínimo).
FONTS = [
    ('italic', 'latin', 'sub-3.woff2'),    # fraunces-3 = italic LATIN (o mapa antigo trocava!)
    ('normal', 'latin', 'sub-4.woff2'),    # fraunces-4 = LATIN de verdade
]
UR = {
    'latin': "U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD",
    'latin-ext': "U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1D00-1DBF, U+1E00-1E9F, U+1EF2-1EFF, U+2020, U+20A0-20AB, U+20AD-20C0, U+2113, U+2C60-2C7F, U+A720-A7FF",
}

def main():
    html = (SRC / 'template.html').read_text(encoding='utf-8')

    css = "\n".join(
        f"@font-face{{font-family:'Fraunces';font-style:{st};font-weight:300 700;font-display:swap;"
        f"src:url({b64(ASSETS / 'fonts' / f, 'font/woff2')}) format('woff2');unicode-range:{UR[sub]};}}"
        for st, sub, f in FONTS)
    html = html.replace('{{FONTS}}', css)

    G = ROOT / 'node_modules' / 'gsap' / 'dist'
    html = html.replace('{{GSAP}}', (G / 'gsap.min.js').read_text())
    html = html.replace('{{SCROLLTRIGGER}}', (G / 'ScrollTrigger.min.js').read_text())
    html = html.replace('{{SCROLLSMOOTHER}}', (G / 'ScrollSmoother.min.js').read_text())
    html = html.replace('{{SPLITTEXT}}', (G / 'SplitText.min.js').read_text())

    for key in sorted(set(re.findall(r'\{\{IMG:([\w\-]+)\}\}', html))):
        f = ASSETS / 'photos-webp' / f'{key}.webp'
        if not f.exists(): sys.exit(f'✗ foto ausente: {f}')
        n = html.count(f'{{{{IMG:{key}}}}}')
        if n > 2: sys.exit(f'✗ foto {key} usada {n}× (>2)')
        html = html.replace(f'{{{{IMG:{key}}}}}', b64(f, 'image/webp'))

    for key in sorted(set(re.findall(r'\{\{BRAND:([\w\-]+)\}\}', html))):
        f = ASSETS / 'brand' / f'{key}.png'
        if not f.exists(): sys.exit(f'✗ asset ausente: {f}')
        html = html.replace(f'{{{{BRAND:{key}}}}}', png_small(f))

    assert '{{' not in re.sub(r'\{\{(?:IMG|BRAND|FONTS|GSAP|SCROLLTRIGGER|SCROLLSMOOTHER|SPLITTEXT)', '', html) or True
    if re.search(r'\{\{(?!IMG:|BRAND:)', html): sys.exit('✗ placeholder não resolvido')
    OUT.write_text(html, encoding='utf-8')
    print(f'✓ {OUT.name} — {OUT.stat().st_size/1048576:.2f} MB')

if __name__ == '__main__':
    main()
