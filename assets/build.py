"""Generates the profile README SVGs (CoreMesh style). Run: python3 assets/build.py
Everything shown is real: projects, merged PRs and links come from the README text."""
from pathlib import Path
from xml.sax.saxutils import escape as e

OUT = Path(__file__).resolve().parent
BG, PANEL, LINE, INK, DIM, LIME, OLIVE = "#0A0B0F", "#12141A", "#262A33", "#EEF0E8", "#8A909C", "#C9F26B", "#9DBE4A"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"


def mesh(x, y, s=1.0, wave=True):
    """The CoreMesh mascot (same shapes as the site), right arm waving."""
    arm = (f'<g class="arm"><rect x="53" y="33" width="8" height="15" rx="4" fill="{LIME}"/>'
           f'<circle cx="57" cy="49" r="4.6" fill="{LIME}"/></g>')
    return f'''<g transform="translate({x},{y}) scale({s})">
  <g class="bob">
  <path d="M32 14V5" stroke="{LIME}" stroke-width="2.4" stroke-linecap="round"/>
  <circle cx="32" cy="5" r="3.6" fill="{BG}" stroke="{LIME}" stroke-width="2.2"/>
  <circle class="blinkdot" cx="32" cy="5" r="1.4" fill="{LIME}"/>
  <rect x="21" y="58" width="7" height="15" rx="3.5" fill="{OLIVE}"/><rect x="18" y="70" width="12" height="6" rx="3" fill="{OLIVE}"/>
  <rect x="36" y="58" width="7" height="15" rx="3.5" fill="{OLIVE}"/><rect x="34" y="70" width="12" height="6" rx="3" fill="{OLIVE}"/>
  <rect x="3" y="33" width="8" height="15" rx="4" fill="{LIME}"/><circle cx="7" cy="49" r="4.6" fill="{LIME}"/>
  <rect x="9" y="13" width="46" height="48" rx="14" fill="{LIME}"/>
  <rect x="14" y="19" width="36" height="27" rx="9" fill="{BG}"/>
  <g class="eyes"><rect x="21" y="26" width="6" height="9" rx="3" fill="{LIME}"/><rect x="37" y="26" width="6" height="9" rx="3" fill="{LIME}"/></g>
  <path d="M28 39.5q4 3 8 0" fill="none" stroke="{LIME}" stroke-width="2" stroke-linecap="round"/>
  {arm if wave else ''}
  </g>
</g>'''


STYLE = f"""<style>
  .t{{font-family:{MONO};fill:{INK}}} .d{{fill:{DIM}}} .l{{fill:{LIME}}}
  .s{{font-family:{SANS};}}
  .ln{{opacity:0;animation:in .35s ease-out forwards}}
  @keyframes in{{from{{opacity:0;transform:translateY(4px)}}to{{opacity:1;transform:none}}}}
  .cur{{animation:blink 1s steps(1) infinite}} @keyframes blink{{50%{{opacity:0}}}}
  .arm{{transform-origin:57px 36px;animation:wave 2.4s ease-in-out infinite}}
  @keyframes wave{{0%,60%,100%{{transform:rotate(0)}}70%{{transform:rotate(-150deg)}}80%{{transform:rotate(-115deg)}}90%{{transform:rotate(-150deg)}}}}
  .bob{{animation:bob 3s ease-in-out infinite}} @keyframes bob{{50%{{transform:translateY(-2px)}}}}
  .eyes{{transform-origin:32px 30px;animation:eyes 4s infinite}} @keyframes eyes{{0%,46%,50%,100%{{transform:scaleY(1)}}48%{{transform:scaleY(.1)}}}}
  @media (prefers-reduced-motion:reduce){{*{{animation:none!important}} .ln{{opacity:1}}}}
</style>"""


def frame(w, h, title, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{e(title)}">
{STYLE}
<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="14" fill="{BG}" stroke="{LINE}"/>
{body}
</svg>'''


def header():
    w, h = 840, 300
    lines = [
        ("t d", 24, "$ mesh --whoami"),
        ("t l big", 44, "Indra Wijaya"),
        ("t", 16, "> backend & developer-tooling engineer · CI/CD · automation"),
        ("t", 16, "> building CoreMesh: AI-drafted guides, fact-checked first"),
        ("t", 16, "> I verify every change end to end before I submit it"),
    ]
    body = [f'<rect x="1" y="1" width="{w-2}" height="34" rx="13" fill="{PANEL}"/>',
            f'<rect x="1" y="22" width="{w-2}" height="13" fill="{PANEL}"/>',
            '<circle cx="24" cy="18" r="6" fill="#FF5F56"/><circle cx="44" cy="18" r="6" fill="#FFBD2E"/><circle cx="64" cy="18" r="6" fill="#27C93F"/>',
            f'<text class="t d" x="{w//2}" y="23" font-size="13" text-anchor="middle">indra@coremesh: ~</text>']
    y, delay = 82, 0.1
    for cls, size, txt in lines:
        weight = ' font-weight="700"' if "big" in cls else ""
        body.append(f'<g class="ln" style="animation-delay:{delay:.2f}s"><text class="{cls.replace(" big","")}" x="32" y="{y}" font-size="{size}"{weight}>{e(txt)}</text></g>')
        y += 50 if "big" in cls else (52 if size == 24 else 30)
        delay += 0.45
    body.append(f'<g class="ln" style="animation-delay:{delay:.2f}s"><text class="t d" x="32" y="{y+10}" font-size="16">$ <tspan class="cur l">▌</tspan></text></g>')
    body.append(mesh(722, 120, 1.5))
    return frame(w, h, "Indra Wijaya — backend and developer-tooling engineer building CoreMesh", "\n".join(body))


def link(label, handle):
    w, h = 196, 56
    body = f'''<text class="s" x="20" y="24" font-size="15" font-weight="700" fill="{LIME}">{e(label)}</text>
<text class="t d" x="20" y="43" font-size="12">{e(handle)}</text>
<text class="t l" x="{w-26}" y="35" font-size="18">→</text>'''
    return frame(w, h, f"{label}: {handle}", body)


def card(name, line1, line2, tags, badge=None):
    w, h = 410, 150
    tag_svg, x = [], 20
    for t in tags:
        tw = 9 + len(t) * 7.4
        tag_svg.append(f'<rect x="{x}" y="112" width="{tw:.0f}" height="22" rx="11" fill="{PANEL}" stroke="{LINE}"/>'
                       f'<text class="t d" x="{x+tw/2:.0f}" y="127" font-size="11.5" text-anchor="middle">{e(t)}</text>')
        x += tw + 8
    b = (f'<rect x="{w-112}" y="18" width="94" height="22" rx="11" fill="{LIME}"/>'
         f'<text class="s" x="{w-65}" y="33" font-size="11.5" font-weight="700" text-anchor="middle" fill="{BG}">{e(badge)}</text>') if badge else ""
    body = f'''<text class="s" x="20" y="36" font-size="21" font-weight="800" fill="{INK}">{e(name)}</text>{b}
<text class="s" x="20" y="68" font-size="13.5" fill="{DIM}">{e(line1)}</text>
<text class="s" x="20" y="88" font-size="13.5" fill="{DIM}">{e(line2)}</text>
{''.join(tag_svg)}'''
    return frame(w, h, f"{name}. {line1} {line2}", body)


def contributions():
    rows = [("Perenna-Labs/perenna-contracts", "Rust · Soroban", "#140 #157 #158", "3 merged"),
            ("Presago-Labs/presago-contracts", "Rust", "#102 #103", "2 merged"),
            ("Presago-Labs/presago", "JavaScript", "#132", "1 merged"),
            ("BasedHardware/omi", "Python", "#21133", "in review")]
    w, h = 840, 70 + 44 * len(rows)
    body = [f'<text class="t d" x="28" y="40" font-size="16">$ gh pr list --author indra112f --state all</text>']
    y = 84
    for i, (repo, lang, prs, state) in enumerate(rows):
        col = LIME if "merged" in state else DIM
        body.append(f'<g class="ln" style="animation-delay:{0.15+i*0.25:.2f}s">'
                    f'<text class="t" x="28" y="{y}" font-size="15">{e(repo)}</text>'
                    f'<text class="t d" x="390" y="{y}" font-size="13">{e(lang)}</text>'
                    f'<text class="t d" x="540" y="{y}" font-size="13">{e(prs)}</text>'
                    f'<text class="t" x="{w-28}" y="{y}" font-size="13" text-anchor="end" style="fill:{col}">{e(state)}</text></g>')
        y += 44
    return frame(w, h, "Open-source contributions: 6 merged pull requests across Perenna-Labs and Presago-Labs, 1 in review at BasedHardware/omi", "\n".join(body))


if __name__ == "__main__":
    (OUT / "header.svg").write_text(header())
    for slug, label, handle in [("site", "CoreMesh", "coremesh.online"), ("dev", "DEV", "@coremesh_team"),
                                ("x", "X", "@CoreMesh_Team"), ("threads", "Threads", "@coremesh_official")]:
        (OUT / f"link-{slug}.svg").write_text(link(label, handle))
    (OUT / "card-claimcheck.svg").write_text(card("claimcheck", "Fact-checks AI-written drafts against their",
                                                  "own sources with Gemma. Quotes verified verbatim.",
                                                  ["Python", "Gemma 4", "MIT"], badge="NEW"))
    (OUT / "card-instant.svg").write_text(card("CoreMesh Instant", "Utility APIs (URL health, TLS/DNS, JSON repair)",
                                               "paid per call over HTTP 402 with USDC on Base.",
                                               ["FastAPI", "nginx", "HTTP 402"], badge="LIVE"))
    (OUT / "contributions.svg").write_text(contributions())
    print("ok")
