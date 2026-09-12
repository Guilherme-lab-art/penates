---
# gstack: design-md-format=spec
name: penates
typography:
  display:
    fontFamily: Fraunces
    fontVariation: opsz 144
    weight: 390
    note: "uma família só, eixos ópticos fazem a hierarquia"
  body:
    fontFamily: Fraunces
    fontVariation: opsz 11
    weight: 400
  label:
    fontFamily: Fraunces
    fontVariation: opsz 14
    weight: 500
    tracking: .22em
    case: upper
  quote:
    fontFamily: Fraunces
    fontVariation: opsz 144
    weight: 380
    style: italic
colors:
  paper: "#F3EBDE"
  paper-deep: "#ECE1CE"
  ink: "#33302A"
  ink-soft: "#636058"
  amber: "#8C3F22"
  amber-soft: "#A9603C"
  hair: "rgba(51,48,42,.22)"
  cine:
    text: "#F3EBDE"
    veil: "rgba(28,24,19,.46-.78)"
    focus: "radial rgba(19,13,8,.52-,.66)"
  provenance: "papel/tinta medidos nos arquivos da marca (logo, figurinhas); âmbar das brasas reais — nunca default"
motion:
  desktop:
    scrub: .55
    pin-durations: "feu 150% · jardin 130% · foyer 120%"
    entrance-ease: "expo.out (display) / power2.out (corpo)"
    hero-settle: "3.2s expo.out, escala 1.16→1.04"
    stamp: "back.out(1.6)"
    breathing: "sine.inOut 4.5-6.5s (figurinhas), 5.5s (logo hero)"
  touch:
    pins: none
    filters: none
    entrances: "0.8-1.5s power2/power3, toggleActions reverse"
  reduced-motion: "estático total, stills visíveis"
photo:
  width: 720px
  rule: "moldura editorial (passe-partout) no desktop; sangria total no mobile; nunca esticar"
  uses-per-photo: 2
  numbering: "planches fig. 01-14 sequenciais; cenas de cinema usam slate no canto"
  text-over-photo: "proibido exceto em cena cine com véu medido"
ban-list:
  - pills/badges de feature
  - botão CTA com seta
  - footer SaaS 4 colunas
  - "seções numeradas tipo passo de app (01/02/03)"
  - gradientes decorativos
  - fade-slide genérico em tudo
  - scroll-jack
  - template/gerador de UI
gates:
  contrast: "≥4.5:1 medido por pixel atrás do texto"
  cls: 0
  js-errors: 0
  external-resources: 0
  overflow-x: 0
  touch-fps: "p95 ≤ 17ms"
---

# Design System — Pénates

## Overview

- **O que é:** one-page do restaurante Pénates — 226 boulevard Voltaire, Paris 11ᵉ
- **Para quem:** a cheffe Stéphanie Moquet (primeira address pessoal, pós-groupe Fuga) e o público francês do 11ᵉ
- **Espaço/indústria:** bistrô de fogo — robata, potager, caves vivantes (peers: Le Bernardin, SingleThread, Adachi)
- **Tipo de projeto:** pitch de venda — o decisor abre no celular

## Direction

**Um livro de artista que, em quatro momentos, vira cinema.** O papel é a toalha
de mesa; as fotos são planches numeradas de livro; LE FEU, LE JARDIN, LES
SIGNATURES e LE FOYER abrem em cenas full-bleed com véus medidos. O ritmo
livro↔cinema é o que impede "galeria" e "slideshow" ao mesmo tempo.

- **Decoration level:** intencional e escasso — grão quase imperceptível global, hairlines, um acento âmbar (≤5%)
- **Mood:** fogo doméstico. Sereno, não minimalista; francês, não SaaS

## Voice

Francês editorial. Citações com «guillemets», definição em itálico, phonétique
[pe.nat]. Legendas em caixa alta espaçada com número de planche em âmbar.
Placeholders provisórios sempre visíveis como *(légende à venir)* — nunca
parecem prontos, nunca inventam.

## Sistema fotográfico

Fotos reais da casa, todas 720px. Cada uma recebe posição papelada e número
(fig. 01–14). Máx. 2 usos por foto (MD5 verificado). Em cenas de cinema a foto
é o mundo; a planche vira slate de canto. Contraste do texto garantido por véu
+ vinheta de foco, medidos por pixel.

## Motion — a regra de ouro

Uma coreografia por momento, nunca efeito espalhado. Desktop: pins com scrub
.55. Touch: scroll 100% nativo, zero pins, zero filtros, entradas coreografadas
ao chegar. Reduced-motion: stills estáticos, tudo visível. Nada de loop no hero.
