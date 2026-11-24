# Bios Therapy XII — Landing Page

Remontagem fiel de **https://drluisaugustoc.com.br/** em HTML/CSS/JS estático,
sem dependências de build. Basta abrir `index.html` ou subir esta pasta em
qualquer hospedagem.

## Estrutura

```
./
├── index.html            Landing page completa (todas as seções do original)
├── design-system.html    Guia visual: cores, tipografia e os 13 ícones SVG
├── css/
│   ├── styles.css         Tokens + layout da landing
│   └── design-system.css  Estilos do guia
├── js/
│   └── main.js            Tabs (artigos), acordeão (FAQ), reveal on scroll, vídeos
└── assets/
    ├── icons/             13 ícones SVG + sprite.svg (design system)
    ├── icons-src/         PNGs originais dos ícones (referência p/ refino)
    └── img/               Imagens baixadas do site original
```

## Paleta e fontes (extraídas do CSS original — Elementor)

| Token          | Hex       | Uso                        |
|----------------|-----------|----------------------------|
| `--green`      | `#26c484` | acento, títulos            |
| `--green-neon` | `#1fff8c` | destaques, preço, hover    |
| `--green-btn`  | `#04b33a` | botões                     |
| `--green-deep` | `#265f2a` | blocos verdes (público)    |
| `--bg`         | `#00292b` | fundo principal            |
| `--bg-deep`    | `#030806` | seções alternadas          |
| `--surface`    | `#051b11` | cards                      |

Fontes: **League Spartan** (títulos), **Roboto** (corpo), **Roboto Slab** (código).
Carregadas via Google Fonts.

## Ícones — design system em SVG

Os 13 ícones de benefício do site original eram PNGs. Foram **redesenhados como
ícones de linha em SVG**, com padrão único:

- `viewBox="0 0 64 64"`, `stroke-width="3"`, pontas/junções arredondadas
- cor via `currentColor` (herda do container — hoje `--green`)
- disponíveis de 3 formas:
  1. **Sprite inline** no `<body>` do `index.html` → `<svg><use href="#ic-epiderme"/></svg>`
  2. **`assets/icons/sprite.svg`** (mesmo sprite, arquivo único)
  3. **Arquivos soltos** `assets/icons/*.svg` → `<img src="assets/icons/epiderme.svg">`

| id                | Significado                         |
|-------------------|------------------------------------|
| `ic-epiderme`     | Penetra epiderme / derme           |
| `ic-ph`           | Controla o pH                      |
| `ic-drenagem`     | Possibilita a drenagem             |
| `ic-dor`          | Controla inflamação e dor          |
| `ic-circulacao`   | Circulação e oxigenação            |
| `ic-mitocondria`  | Metabolismo mitocondrial           |
| `ic-colageno`     | Produz colágeno                    |
| `ic-cicatriza`    | Regenera e cicatriza               |
| `ic-reduzirmedidas` | Reduz medidas                    |
| `ic-flacidez`     | Controla a flacidez                |
| `ic-linhas`       | Linhas de expressão e rugas        |
| `ic-pelesuave`    | Suaviza a pele                     |
| `ic-celulite`     | Celulite e estrias                 |

> São um **primeiro traçado** para você refinar. `assets/icons/gen_icons.py`
> regenera os arquivos e o `sprite.svg` a partir de um único dicionário de
> paths — bom ponto de partida para padronizar o conjunto.
> Os PNGs originais ficaram em `assets/icons-src/` para comparação.

## O que ainda precisa dos arquivos originais

- **Vídeo do hero (VSL)** — já ligado ao YouTube `UoHzy4hWiq8`
  (`https://www.youtube.com/watch?v=UoHzy4hWiq8`). Thumbnail salvo em
  `assets/img/vsl-poster.jpg`; o clique injeta o `<iframe>` com autoplay.
- **3 vídeos de depoimento** — ainda placeholder (bloco com ▶). Preencha
  `data-embed="https://www.youtube.com/embed/ID"` nas 3 `<div class="video">`
  da seção *Depoimentos*.
- Se tiver as versões em alta das imagens (foto do Dr., mockup do curso, patente),
  substitua os arquivos em `assets/img/` mantendo o nome.

Imagens já incluídas: `BiosTherapy.png`, `Patente.png`, `curso.webp`,
`selo100.png` (100% Secure), `Cadeado.webp` (escudo), `Dep01–04.png`,
`vsl-poster.jpg`.

## Links externos usados

- Compra (Yampi): `https://bios-fototerapia.pay.yampi.com.br/r/IZKE2UZZ4H`
- WhatsApp: `https://wa.me/5511971975525`

## Layout e espaçamento (alinhado ao print)

- **Estética quadrada**: `--radius: 0` — nenhum canto arredondado em cards,
  botões, molduras, play de vídeo ou botão flutuante.
- **Fundo único**: todas as seções usam o teal `--bg` (#00292b), como a hero.
  O contraste vem de caixas pretas (`#030806`), cards verdes e molduras verdes —
  não há alternância de fundo.
- **Hero** em coluna única centrada, na proporção do print: título ▸ VSL
  (máx. 900 px, 16:9, botão play vermelho estilo YouTube) ▸ parágrafo.
  Sem botão de CTA (o original não tem).
- **Benefícios**: 4 colunas (2 tablet / 1 mobile), cards **transparentes** só
  com borda verde.
- **Conheça / Certificado de Patente / Como sei que…**: imagem à esquerda,
  texto à direita; molduras verdes (`.figure-frame--green`, `.framed`).
- **Para Profissionais**: caixa preta de introdução + **5 cards** com filete
  verde à esquerda. **Para o Público**: caixa preta + 6 cards verdes chapados.
- **Regra de UI — entrelinha 150%**: todo corpo de texto usa `line-height: 1.5`;
  títulos entre `1.12` e `1.28`. Documentado no componente **Espaçamentos** de
  `design-system.html` (tabela de line-heights + escala de 4 px + tokens).

## Observações de fidelidade

- Estrutura, ordem das seções, textos e preços seguem o original.
- A seção *Artigos Científicos* é um componente de **abas** (7 categorias).
- Rodapé fixo em "2025", como no original.
- Layout responsivo (grelhas colapsam para 1 coluna no mobile).
