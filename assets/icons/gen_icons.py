#!/usr/bin/env python3
"""Gera os 13 icones SVG do design system Bios Therapy + um sprite unico."""
import os, pathlib

OUT = pathlib.Path(r"c:/Projetos/DrConrado/site/assets/icons")
OUT.mkdir(parents=True, exist_ok=True)

# id -> (titulo, conteudo interno do <svg> / <symbol>)
ICONS = {
"epiderme": ("Penetra epiderme e derme", """
  <path d="M32 6c0 0-11 13-11 20a11 11 0 0 0 22 0c0-7-11-20-11-20Z"/>
  <path d="M11 27h42v21a4 4 0 0 1-4 4H15a4 4 0 0 1-4-4Z"/>
  <path d="M11 42h42"/>
"""),
"ph": ("Controla o pH", """
  <path d="M27 7c0 0-14 17-14 27a14 14 0 0 0 28 0c0-4-2-9-5-13"/>
  <text x="27" y="41" text-anchor="middle" font-family="'League Spartan',Arial,sans-serif" font-size="15" font-weight="700" fill="currentColor" stroke="none">pH</text>
  <path d="M47 37c0 0-6 7-6 11a6 6 0 0 0 12 0c0-4-6-11-6-11Z"/>
"""),
"drenagem": ("Possibilita a drenagem", """
  <path d="M32 7c0 0-7 9-7 13a7 7 0 0 0 14 0c0-4-7-13-7-13Z"/>
  <path d="M12 26h40l-3 24a4 4 0 0 1-4 3H19a4 4 0 0 1-4-3Z"/>
  <path d="M12 26h40"/>
  <path d="M23 32v16M31 32v18M39 32v16M47 32v13"/>
"""),
"dor": ("Controla inflamacao e dor", """
  <path d="M15 44a15 15 0 1 1 26 0"/>
  <path d="M14 46h28"/>
  <path d="M20 28l7 3M35 28l-7 3"/>
  <circle cx="23" cy="36" r="1.6" fill="currentColor" stroke="none"/>
  <circle cx="33" cy="36" r="1.6" fill="currentColor" stroke="none"/>
  <path d="M24 42q4 3 8 0"/>
  <path d="M8 22l6 3-3 4 6 3"/>
  <path d="M50 20l-6 3 3 4-6 3"/>
"""),
"circulacao": ("Melhora circulacao e oxigenacao", """
  <path d="M8 17q8-7 16 0t16 0 16 0"/>
  <path d="M8 47q8-7 16 0t16 0 16 0"/>
  <circle cx="20" cy="30" r="4"/>
  <circle cx="33" cy="34" r="5"/>
  <circle cx="45" cy="28" r="3.5"/>
  <circle cx="26" cy="41" r="3"/>
  <circle cx="41" cy="41" r="3.5"/>
"""),
"mitocondria": ("Estimula o metabolismo mitocondrial", """
  <path d="M23 19C11 21 8 37 17 45c9 9 31 8 36-5C57 27 45 15 34 19c-4 1-7 1-11 0Z"/>
  <path d="M18 29q7 5 14 0t13 0"/>
  <path d="M18 38q7 5 14 0t12 0"/>
  <circle cx="15" cy="15" r="4"/>
"""),
"colageno": ("Produz colageno", """
  <circle cx="27" cy="19" r="9"/>
  <text x="27" y="24" text-anchor="middle" font-family="'League Spartan',Arial,sans-serif" font-size="12" font-weight="700" fill="currentColor" stroke="none">C</text>
  <path d="M34 13l7-4"/>
  <circle cx="45" cy="8" r="3.2"/>
  <path d="M8 35q6-4 12 0t12 0 12 0 11 0"/>
  <g fill="currentColor" stroke="none">
    <circle cx="12" cy="43" r="1.6"/><circle cx="22" cy="43" r="1.6"/><circle cx="32" cy="43" r="1.6"/><circle cx="42" cy="43" r="1.6"/><circle cx="52" cy="43" r="1.6"/>
    <circle cx="17" cy="51" r="1.6"/><circle cx="27" cy="51" r="1.6"/><circle cx="37" cy="51" r="1.6"/><circle cx="47" cy="51" r="1.6"/>
  </g>
"""),
"cicatriza": ("Regenera e cicatriza o tecido", """
  <circle cx="27" cy="29" r="17"/>
  <path d="M17 39 39 19"/>
  <path d="M19 33l6 6M23 29l6 6M27 25l6 6M31 21l6 6"/>
  <circle cx="47" cy="45" r="8"/>
  <path d="M44 42l6 6M50 42l-6 6"/>
"""),
"reduzirmedidas": ("Reduz medidas", """
  <path d="M23 12h14v6c6 4 8 15 6 25-1 5-1 9 0 12H17c1-3 1-7 0-12 2-10 0-21 6-25Z"/>
  <path d="M12 33h34v9H12Z"/>
  <path d="M18 33v5M24 33v7M30 33v5M36 33v7M42 33v5"/>
  <path d="M46 32h6v11h-6"/>
"""),
"flacidez": ("Controla a flacidez", """
  <path d="M21 10h18c2 9 5 13 5 22 0 12-5 18-7 27h-6l-2-16-2 16h-6c-2-9-7-15-7-27 0-9 3-13 5-22Z"/>
  <path d="M15 32q-4 5 0 10" stroke-dasharray="2 3"/>
  <path d="M11 30q-4 6 0 13" stroke-dasharray="2 3"/>
  <path d="M50 33l3-4 3 4M53 29v13"/>
"""),
"linhas": ("Reduz linhas de expressao e rugas", """
  <path d="M18 30c0-13 7-21 14-21s14 8 14 21-6 24-14 24-14-11-14-24Z"/>
  <path d="M16 27c2-13 9-19 16-19s14 6 16 19c-4-6-10-9-16-9s-12 3-16 9Z"/>
  <path d="M24 30q3-2 6 0M34 30q3-2 6 0"/>
  <path d="M27 41q5 3 10 0"/>
"""),
"pelesuave": ("Suaviza a pele", """
  <path d="M12 40h40v8a4 4 0 0 1-4 4H16a4 4 0 0 1-4-4Z"/>
  <path d="M12 46h40"/>
  <path d="M14 28q18-16 36 0"/>
  <path d="M44 22l6 3-3 6"/>
  <path d="M20 22l-6 3 3 6"/>
"""),
"celulite": ("Controla celulite e estrias", """
  <path d="M19 11h22c2 8 4 10 4 18 0 13-6 19-8 24h-7l-2-13-2 13h-7c-2-5-8-11-8-24 0-8 2-10 4-18Z"/>
  <path d="M9 30h9M14 26l-5 4 5 4"/>
  <path d="M51 30h-9M46 26l5 4-5 4"/>
  <g fill="currentColor" stroke="none">
    <circle cx="24" cy="34" r="1.5"/><circle cx="20" cy="40" r="1.5"/><circle cx="38" cy="34" r="1.5"/><circle cx="42" cy="40" r="1.5"/><circle cx="31" cy="44" r="1.5"/>
  </g>
"""),
}

HEAD = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none" '
        'stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" '
        'class="bios-icon" role="img" aria-label="{label}">')

for key, (label, body) in ICONS.items():
    svg = HEAD.format(label=label) + body.rstrip() + "\n</svg>\n"
    (OUT / f"{key}.svg").write_text(svg, encoding="utf-8")

# sprite unico com <symbol>
parts = ['<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true">']
for key, (label, body) in ICONS.items():
    parts.append(f'  <symbol id="ic-{key}" viewBox="0 0 64 64">')
    parts.append(f'    <title>{label}</title>')
    parts.append(body.rstrip("\n"))
    parts.append('  </symbol>')
parts.append('</svg>\n')
(OUT / "sprite.svg").write_text("\n".join(parts), encoding="utf-8")

print("gerados:", ", ".join(f"{k}.svg" for k in ICONS), "+ sprite.svg")
print("total:", len(ICONS), "icones")
