# Pénates — Análise & Direção (11/09/2026)

Base: 23 arquivos enviados + `conhecimento-penates.md` (público). Análise por pixels
(PIL), OCR (RapidOCR), nitidez (Laplaciano), pHash. **Nenhum conteúdo foi inventado** —
o que não é verificável está marcado como provisório.

---

## 1 · Melhor tipo de site — VEREDITO

**One-page editorial imersivo** — um "livro que se desenrola": fundo papel, fotos em
molduras, 8 movimentos, mobile como experiência principal. **Não** multi-page clássico,
**não** landing de app, **não** dark-mode genérico.

**Por quê (fatos, não gosto):**

| Fato | Consequência |
|---|---|
| Menu, preços e horários **não existem publicamente** ainda | Site institucional multi-page teria páginas vazias; one-page narra sem depender disso |
| 17 fotos reais, todas **verticais 720px** | Composição em molduras editoriais — nunca esticadas full-bleed no desktop |
| Único canal de reserva = **Instagram (@penates_paris)** | Um CTA único, repetido com elegância |
| A marca tem **história real de sustentabilidade** (potager, circuits courts) | Narrativa story-driven — 73% dos consumidores preferem restaurantes eco-conscientes [2] |
| 72% das buscas de restaurante acontecem no smartphone [2] | Mobile-first de verdade, não adaptado |
| Fine dining de referência: "deixe fotografia e espaço negativo falarem" (Atelier Crenn) [4] | Whitespace generoso, tipografia com presença |

Referências de tom: Le Bernardin (minimalismo + tipografia elegante), Eleven Madison
Park (espaço negativo + tela cheia), SingleThread (narrativa da fazenda ≈ nosso
potager), Adachi (serenidade japonesa — casa com a influência japonesa da cozinha).

**MCP 21st consultado** ("restaurant premium hero"): os componentes prontos são heroes
genéricos de SaaS (fundo animado preto/branco etc.) — **nenhum serve**. Confirma a
construção artesanal. As regras de qualidade dos skills Vercel seguem valendo como
critério (contraste medido, estados, reduced-motion, 44px, sem dead-ends).

---

## 2 · O design autêntico da marca — o que os pixels dizem

O logo e as 5 figurinhas vivem sobre o **mesmo papel marfim em todos os arquivos**:

```
PAPEL   #F3EBDE  rgb(243,235,222)   ← fundo do site inteiro (a "toalha de papel")
TINTA   #636058 / #7E7971           ← texto e ilustrações (cinza-oliva quente)
ÂMBAR   #7E3918 #CB8A48 #E7AC47     ← o fogo (Grela, 074949) — acento RARO (≤5%)
FOLHA   #2C2A1A #5A5542             ← a mesa/posta verde (172839)
MADEIRA #643215 #80532D             ← a estante (Estante.jpg)
```

**Sistema:** papel como superfície · tinta como palavra · âmbar como brasa pontual ·
verde como contraponto. Tipografia serifada editorial (display) + sans discreta —
**em francês**. Zero gradientes, zero pills, zero linguagem de app.

**Assets já extraídos** (tinta → PNG transparente, prontos para animar):
`penates-site/assets/brand/` — `logo-simbolo.png` (480×702, emblema vertical único,
aspecto 0.43) · `figurinha-a` (352×351) · `figurinha-b` (432×449) · `figurinha-c`
(176×536, alta e estreita) · `figurinha-d-wordmark.png` (496×160, OCR "tenates").

---

## 3 · As fotos — análise e posição (a alma)

Regra técnica geral: **todas têm 720px de largura** → sempre em moldura, no desktop
nunca esticadas além de ~1100px de largura com tratamento suave (grão leve); watermark
IG fica nas bordas → crop interior seguro de 92%. Máx. 2 usos por foto.

### Identificadas com confiança

| # | Arquivo | O que os dados mostram | POSIÇÃO | Tratamento |
|---|---|---|---|---|
| 1 | `Grela.jpg` | Robata; laranjas vivos #E7AC47; nitidez 1921 | **01 LE NOM — hero** | Moldura central alta; reveal com scrim que cede |
| 2 | `172943` | Braises âmbar; "tenates"; lum 108; soft (580) | **02 LE FEU** | Fundo atmosférico + véu escuro p/ texto |
| 3 | `172802` | Cozinha escura; "enat"; nitidez 1547 | **03 LA CUISINE** | Recorte vertical + parallax |
| 4 | `192847` | Verde denso; "Incroyable"; **a mais nítida (3448)** | **04 LE JARDIN** | Macro grande — folhagem em detalhe |
| 5 | `172839` | Mesa posta, verdes + linho; nitidez 2438 | **05 LA TABLE** | Moldura clássica, mão direita |
| 6 | `172929` | **Cartão LES SIGNATURES** (OCR: Negroni, Terre & Feu, Ignis Foci + ingredientes) | **06 LES SIGNATURES** | Tratar como **carta**, não foto: transcrever tipograficamente + miniatura do original |
| 7 | `Estante.jpg` | Prateleira LOW/NO APERITIF SPRITZ + "BARBACOA"; nitidez 1302 | **06 LES SIGNATURES** | Apoio — os espelhos sem álcool |
| 8 | `193044` | **Vinho real: Domaine de la Janasse, Châteauneuf-du-Pape 2014**; nitidez 1561 | **07 LES VINS** | Única foto de vinho — protagonista da seção |
| 9 | `1789096220204` | Salle bege, difusa (362) | **L'ARRIVÉE** (topo, antes do fogo) | Atmosfera — pequena, respirando |
| 10 | `074749` | Âmbar profundo; @penates_paris; lum 100 | **08 LE FOYER — clímax/fecho** | Fecha a narrativa com a brasa |

### Provisórias — peço legenda de 1 linha para cravar

| Arquivo | Sinal | Posição provisória |
|---|---|---|
| `192951` / `192926` | Azul-aço (irmãs, cenas diferentes d=103) | Sala à noite / cozinha — LA MAISON |
| `193017` / `193004` | Cinzas difusas | Atmosfera interior |
| `172813` | Salle clara + azul, difusa (253) | L'Arrivée 2 / véranda |
| `172745` | Terracota clara, média nitidez | Detalhe — cozinha |
| `172709` | Creme, 4:5 | Detalhe — sobremesa? |

*Omitidas do site por enquanto: nenhuma — todas têm lugar assim que confirmadas.*

---

## 4 · As figurinhas — como vivem (premium, essência intacta)

O truque que preserva a essência **por construção**: o fundo do site É o mesmo papel
marfim #F3EBDE — as figurinhas (extraídas como tinta transparente) pousam nele como
se tivessem sido desenhadas na própria página. Nada de recorte duro visível, nada de
filtro.

**Coreografia (GSAP, tudo lento e caro):**

- **Entrada:** fade + settle — `scale 1.04→1`, 0.9s, `power2.out` — como um carimbo
  pousando no papel
- **Vida:** float contínuo `y ±6px` / rotação `±1.5°`, 5–7s, `sine.inOut` yoyo —
  respiração, nunca pulinho
- **Scroll:** parallax lento (±30px), cada uma em velocidade própria
- **Jamais:** bounce elástico, giro, mudança de cor, sombra dura — nada de
  sticker-de-app
- `prefers-reduced-motion`: estáticas, sempre visíveis

**Posições:**

| Asset | Onde |
|---|---|
| `logo-simbolo` | Hero (pequeno, acima do nome) · rodapé · favicon |
| `figurinha-d-wordmark` | O fecho, antes do rodapé — assinatura |
| `figurinha-a` / `figurinha-b` | Margens das seções Cuisine / Jardin / Table — acentos |
| `figurinha-c` (alta e estreita) | Acompanha LES VINS em contra-ponto vertical |

`Figurinha1.jpg` é um screenshot de story real ("J-11 pour les becs sucrés", 28/08 —
countdown para os doces): fica como **referência de calendário**, não vira asset.

---

## 5 · Estrutura — 8 movimentos

```
01 LE NOM          logo-símbolo + PÉNATES + [pe.nat] + hero Grela em moldura
02 LE FEU          braises 172943 + « La robata — un grill à charbon ouvert sur la salle »
03 LA CUISINE      172802 + filosofia real (potager, circuits courts, saisons)
04 LE JARDIN       macro 192847 — a folhagem mais nítida que temos
05 LA TABLE        172839 — a mesa posta
06 LES SIGNATURES  transcrição tipográfica do cartão + Estante (miroirs sans alcool)
07 LES VINS        193044 Janasse CdP 2014 — « verre après verre »
08 LE FOYER        074749 âmbar + wordmark-d + CTA Instagram + endereço real
```

Mobile = composição própria (molduras em coluna, fotos podem sangrar a tela inteira),
desktop = página editorial com margens generosas.

---

## 6 · Próximo passo

Construir o one-page (single-file, fontes subset, GSAP+ScrollTrigger, tudo inline,
QA Playwright: overflow, reduced-motion, contraste, ≤2 usos por foto). As 5 provisórias
entram nas posições provisórias — você corrige no storyboard com uma linha cada.
