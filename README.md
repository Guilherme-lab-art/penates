# Pénates — maison, Paris 11e

🔗 **O site está no ar aqui: https://guilherme-lab-art.github.io/penates/**

(Esta página mostra o código-fonte — o site renderizado, com fotos e animações, vive no link acima.)

## O que é cada coisa

| Arquivo | O que é |
|---|---|
| `index.html` | **O site completo** — fotos e fontes embutidas. É isto que o GitHub Pages serve. |
| `src/template.html` | O molde editável — cada foto é um `{{IMG:…}}` de propósito |
| `src/build.py` | Derrete molde + fotos + fontes → `index.html` (arquivo único) |
| `DESIGN.md` | Fonte da verdade do design (valores medidos) |
| `qa/` *(fora daqui)* | Baterias de verificação: motion, contraste, botões, boot |

## Atualizar o site

```bash
python3 src/build.py   # reconstrói o index.html
git add -u && git add README.md
git commit -m "vN · …"
git push --force <origin> master:main
git reset --mixed a7f0560   # working tree volta a ser a base editável
```

Cuisine ardente · table vivante · jardin caché — MMXXVI
