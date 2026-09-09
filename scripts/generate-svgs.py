#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Generate Code 128 barcodes and system SVGs. Run from repo root."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
DIAG = ASSETS / "diagrams"

# Code 128 patterns: six widths (bar, space, bar, space, bar, space). Sum = 11.
# Stop (106) is 7 widths, sum = 13.
PATTERNS = [
    "212222", "222122", "222221", "121223", "121322", "131222", "122213", "122312",
    "132212", "221213", "221312", "231212", "112232", "122132", "122231", "113222",
    "123122", "123221", "223211", "221132", "221231", "213212", "223112", "312131",
    "311222", "321122", "321221", "312212", "322112", "322211", "212123", "212321",
    "232121", "111323", "131123", "131321", "112313", "132113", "132311", "211313",
    "231113", "231311", "112133", "112331", "132131", "113123", "113321", "133121",
    "313121", "211331", "231131", "213113", "213311", "213131", "311123", "311321",
    "331121", "312113", "312311", "332111", "314111", "221411", "431111", "111224",
    "111422", "121124", "121421", "141122", "141221", "112214", "112412", "122114",
    "122411", "142112", "142211", "241211", "221114", "413111", "241112", "134111",
    "111242", "121142", "121241", "114212", "124112", "124211", "411212", "421112",
    "421211", "212141", "214121", "412121", "111143", "111341", "131141", "114113",
    "114311", "411113", "411311", "113141", "114131", "311141", "411131",
    "211412",  # 103 Start A
    "211214",  # 104 Start B
    "211232",  # 105 Start C
    "2331112",  # 106 Stop
]

LPN = "0217123456"  # 0 interline + 217 Thai Airways + 123456 example serial


def code128_c_values(digits: str) -> list[int]:
    if len(digits) % 2:
        raise ValueError("Code 128C needs even digit count")
    values = [105]  # Start C
    for i in range(0, len(digits), 2):
        values.append(int(digits[i : i + 2]))
    checksum = values[0]
    for i, v in enumerate(values[1:], start=1):
        checksum += i * v
    values.append(checksum % 103)
    values.append(106)  # Stop
    return values


def barcode_modules(digits: str) -> list[tuple[int, int]]:
    """Return list of (is_bar, width) module runs."""
    runs = []
    for v in code128_c_values(digits):
        pattern = PATTERNS[v]
        for i, ch in enumerate(pattern):
            runs.append((1 if i % 2 == 0 else 0, int(ch)))
    return runs


def barcode_svg_rects(
    digits: str,
    x: float,
    y: float,
    height: float,
    module: float = 1.15,
    fill: str = "#111111",
) -> tuple[str, float]:
    parts = []
    cx = x
    for is_bar, w in barcode_modules(digits):
        width = w * module
        if is_bar:
            parts.append(
                f'<rect x="{cx:.2f}" y="{y:.2f}" width="{width:.2f}" height="{height:.2f}" fill="{fill}"/>'
            )
        cx += width
    return "\n    ".join(parts), cx - x


def barcode_vertical_rects(
    digits: str,
    x: float,
    y: float,
    width: float,
    module: float = 1.0,
    fill: str = "#111111",
) -> tuple[str, float]:
    parts = []
    cy = y
    for is_bar, w in barcode_modules(digits):
        h = w * module
        if is_bar:
            parts.append(
                f'<rect x="{x:.2f}" y="{cy:.2f}" width="{width:.2f}" height="{h:.2f}" fill="{fill}"/>'
            )
        cy += h
    return "\n    ".join(parts), cy - y


INK = "#111111"
GROUND = "#F7F6F2"
PAPER = "#FFFEFA"
RULE = "#111111"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)}")


def hero() -> None:
    bars, bar_w = barcode_svg_rects(LPN, 742, 148, 118, module=1.28)
    vbars, _ = barcode_vertical_rects(LPN, 64, 118, 22, module=0.85)
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 520" role="img" aria-labelledby="title desc">
  <title id="title">Dr Non’s Luggage Tag Aesthetic — destination BKK dominant, LPN and Code 128 secondary, claim stubs as backup</title>
  <desc id="desc">White thermal baggage tag. Primary: IATA destination BKK. Secondary: 10-digit license plate {LPN} encoded as Code 128C, printed twice at 90 degrees. Tertiary: TG 676, 08SEP26, NRT–BKK. Fallback: ARKARA/NON. Backup: claim and stub receipts.</desc>
  <rect width="1280" height="520" fill="{GROUND}"/>
  <!-- tag body -->
  <rect x="40" y="40" width="1200" height="440" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>
  <!-- loop / punch — attachment domain -->
  <circle cx="88" cy="88" r="18" fill="none" stroke="{INK}" stroke-width="2.5"/>
  <circle cx="88" cy="88" r="7" fill="{GROUND}"/>
  <!-- perforation between loop and face -->
  <g stroke="{INK}" stroke-width="1.2" stroke-dasharray="3 5">
    <line x1="128" y1="56" x2="128" y2="464"/>
  </g>
  <!-- vertical barcode: machine domain, orthogonal backup -->
  {vbars}
  <!-- destination: human primary, IATA three-letter domain -->
  <text x="168" y="268" font-family="Arial Narrow, Arial, Helvetica, sans-serif" font-size="188" font-weight="800" letter-spacing="-8" fill="{INK}">BKK</text>
  <text x="176" y="312" font-family="Arial, Helvetica, sans-serif" font-size="15" font-weight="700" letter-spacing="6" fill="{INK}">BANGKOK · จุดหมาย</text>
  <!-- context: carrier + flight + date domain -->
  <text x="176" y="352" font-family="ui-monospace, Courier New, monospace" font-size="18" fill="{INK}">TG 676  ·  08SEP26  ·  NRT–BKK</text>
  <!-- fallback: passenger name, human backup if systems fail -->
  <text x="176" y="386" font-family="Arial, Helvetica, sans-serif" font-size="16" font-weight="700" letter-spacing="2" fill="{INK}">ARKARA/NON</text>
  <!-- LPN human-readable + barcode: machine key domain -->
  {bars}
  <text x="742" y="292" font-family="ui-monospace, Courier New, monospace" font-size="22" letter-spacing="3" fill="{INK}">{LPN}</text>
  <text x="742" y="318" font-family="Arial, Helvetica, sans-serif" font-size="11" letter-spacing="2.4" fill="{INK}">LICENSE PLATE · CODE 128C · เลขป้าย</text>
  <!-- stubs / claim: detachable backup domain -->
  <g fill="none" stroke="{INK}" stroke-width="1.5">
    <rect x="742" y="348" width="168" height="92"/>
    <rect x="922" y="348" width="136" height="92"/>
    <rect x="1070" y="348" width="130" height="92"/>
  </g>
  <text x="754" y="376" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="700" letter-spacing="1.6" fill="{INK}">CLAIM / ใบรับ</text>
    <text x="754" y="400" font-family="ui-monospace, Courier New, monospace" font-size="12" fill="{INK}">{LPN}</text>
  <text x="754" y="422" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="{INK}">BKK · TG676</text>
  <text x="934" y="376" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="700" letter-spacing="1.6" fill="{INK}">STUB 1</text>
  <text x="934" y="400" font-family="ui-monospace, Courier New, monospace" font-size="12" fill="{INK}">{LPN}</text>
  <text x="934" y="422" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="{INK}">LOAD</text>
  <text x="1082" y="376" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="700" letter-spacing="1.6" fill="{INK}">STUB 2</text>
  <text x="1082" y="400" font-family="ui-monospace, Courier New, monospace" font-size="12" fill="{INK}">{LPN}</text>
  <text x="1082" y="422" font-family="Arial, Helvetica, sans-serif" font-size="11" fill="{INK}">XFER</text>
  <!-- size declaration: this object is a closed package -->
  <text x="176" y="448" font-family="Arial, Helvetica, sans-serif" font-size="10" letter-spacing="1.8" fill="{INK}">FACE 50.8–54 mm · PO COMPLETE · IF PRESENT, REQUIRED</text>
</svg>
'''
    write(ASSETS / "hero-tag.svg", svg)


def mark() -> None:
    bars, _ = barcode_svg_rects(LPN, 36, 210, 36, module=0.72)
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 280" role="img" aria-labelledby="title">
  <title id="title">System mark: BKK destination with LPN barcode</title>
  <rect width="320" height="280" fill="{PAPER}" stroke="{INK}" stroke-width="3"/>
  <circle cx="36" cy="36" r="12" fill="none" stroke="{INK}" stroke-width="2"/>
  <circle cx="36" cy="36" r="4" fill="{GROUND}"/>
  <text x="24" y="168" font-family="Arial Narrow, Arial, Helvetica, sans-serif" font-size="96" font-weight="800" letter-spacing="-4" fill="{INK}">BKK</text>
  {bars}
  <text x="36" y="264" font-family="ui-monospace, Courier New, monospace" font-size="12" letter-spacing="1.5" fill="{INK}">{LPN}</text>
</svg>
'''
    write(ASSETS / "mark.svg", svg)


def anatomy() -> None:
    bars, _ = barcode_svg_rects(LPN, 268, 92, 48, module=0.7)
    vbars, _ = barcode_vertical_rects(LPN, 58, 70, 12, module=0.55)
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 620" role="img" aria-labelledby="title">
  <title id="title">Anatomy of the white baggage tag as an information package</title>
  <rect width="980" height="620" fill="{GROUND}"/>
  <text x="40" y="36" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="700" letter-spacing="2" fill="{INK}">ANATOMY · โครงสร้างป้าย</text>
  <text x="40" y="58" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="{INK}">Every zone is a domain. Empty zone = broken package.</text>
  <!-- tag -->
  <rect x="40" y="80" width="520" height="500" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>
  <circle cx="72" cy="112" r="14" fill="none" stroke="{INK}" stroke-width="2"/>
  <circle cx="72" cy="112" r="5" fill="{GROUND}"/>
  <line x1="100" y1="92" x2="100" y2="568" stroke="{INK}" stroke-width="1" stroke-dasharray="3 4"/>
  {vbars}
  <text x="118" y="210" font-family="Arial Narrow, Arial, Helvetica, sans-serif" font-size="92" font-weight="800" letter-spacing="-3" fill="{INK}">BKK</text>
  <text x="122" y="236" font-family="Arial, Helvetica, sans-serif" font-size="11" letter-spacing="3" fill="{INK}">BANGKOK</text>
  <text x="122" y="268" font-family="ui-monospace, Courier New, monospace" font-size="13" fill="{INK}">TG 676 · 08SEP26 · NRT–BKK</text>
  <text x="122" y="292" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700" letter-spacing="1.5" fill="{INK}">ARKARA/NON</text>
  {bars}
  <text x="268" y="158" font-family="ui-monospace, Courier New, monospace" font-size="13" letter-spacing="1" fill="{INK}">{LPN}</text>
  <g fill="none" stroke="{INK}" stroke-width="1.25">
    <rect x="118" y="430" width="130" height="70"/>
    <rect x="258" y="430" width="130" height="70"/>
    <rect x="398" y="430" width="130" height="70"/>
  </g>
  <text x="128" y="458" font-family="Arial, Helvetica, sans-serif" font-size="10" font-weight="700" fill="{INK}">CLAIM</text>
  <text x="128" y="478" font-family="ui-monospace, Courier New, monospace" font-size="11" fill="{INK}">{LPN}</text>
  <text x="268" y="458" font-family="Arial, Helvetica, sans-serif" font-size="10" font-weight="700" fill="{INK}">STUB</text>
  <text x="408" y="458" font-family="Arial, Helvetica, sans-serif" font-size="10" font-weight="700" fill="{INK}">STUB</text>
  <text x="118" y="548" font-family="Arial, Helvetica, sans-serif" font-size="10" letter-spacing="1" fill="{INK}">FACE STOCK 50.8–54 mm  ·  LOOP ADHESIVE-TO-ADHESIVE</text>

  <!-- callouts -->
  <g font-family="Arial, Helvetica, sans-serif" fill="{INK}">
    <line x1="560" y1="112" x2="620" y2="112" stroke="{INK}" stroke-width="1"/>
    <text x="628" y="108" font-size="13" font-weight="700">1 LOOP / PUNCH</text>
    <text x="628" y="126" font-size="11">Attachment domain. Distributes force across the strip.</text>

    <line x1="560" y1="160" x2="620" y2="168" stroke="{INK}" stroke-width="1"/>
    <text x="628" y="164" font-size="13" font-weight="700">2 ORTHOGONAL BARCODE</text>
    <text x="628" y="182" font-size="11">Machine domain, second axis. Conveyors are 3D.</text>

    <line x1="400" y1="190" x2="620" y2="230" stroke="{INK}" stroke-width="1"/>
    <text x="628" y="226" font-size="13" font-weight="700">3 DESTINATION (PRIMARY)</text>
    <text x="628" y="244" font-size="11">IATA three-letter domain. Human stress-scan first.</text>

    <line x1="400" y1="268" x2="620" y2="286" stroke="{INK}" stroke-width="1"/>
    <text x="628" y="282" font-size="13" font-weight="700">4 CARRIER / FLIGHT / DATE</text>
    <text x="628" y="300" font-size="11">Context domain. Sort without a database.</text>

    <line x1="250" y1="292" x2="620" y2="336" stroke="{INK}" stroke-width="1"/>
    <text x="628" y="332" font-size="13" font-weight="700">5 PASSENGER NAME (FALLBACK)</text>
    <text x="628" y="350" font-size="11">Human backup when LPN and systems fail.</text>

    <line x1="500" y1="120" x2="620" y2="392" stroke="{INK}" stroke-width="1"/>
    <text x="628" y="388" font-size="13" font-weight="700">6 LPN + CODE 128 (SECONDARY)</text>
    <text x="628" y="406" font-size="11">10-digit machine key: lead + issuer + serial.</text>

    <line x1="250" y1="465" x2="620" y2="458" stroke="{INK}" stroke-width="1"/>
    <text x="628" y="454" font-size="13" font-weight="700">7 STUBS / CLAIM</text>
    <text x="628" y="472" font-size="11">Detachable backup. Same identity, smaller size.</text>

    <line x1="300" y1="548" x2="620" y2="520" stroke="{INK}" stroke-width="1"/>
    <text x="628" y="516" font-size="13" font-weight="700">8 MATERIAL / WIDTH</text>
    <text x="628" y="534" font-size="11">Durability is information. Face 50.8–54 mm (Reso 740).</text>
  </g>
</svg>
'''
    write(DIAG / "anatomy.svg", svg)


def hierarchy() -> None:
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 420" role="img" aria-labelledby="title">
  <title id="title">Human scan hierarchy under time pressure, then machine, then durability</title>
  <rect width="980" height="420" fill="{GROUND}"/>
  <text x="40" y="36" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="700" letter-spacing="2" fill="{INK}">SCAN ORDER · ลำดับการอ่าน</text>
  <text x="40" y="58" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="{INK}">Time pressure first. Machine second. Durability and lifecycle last — still mandatory.</text>

  <g font-family="Arial, Helvetica, sans-serif" fill="{INK}">
    <rect x="40" y="84" width="180" height="220" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>
    <text x="56" y="112" font-size="12" font-weight="700" letter-spacing="2">1 PRIMARY</text>
    <text x="52" y="188" font-family="Arial Narrow, Arial, sans-serif" font-size="48" font-weight="800">BKK</text>
    <text x="56" y="220" font-size="11">Human destination</text>
    <text x="56" y="240" font-size="11">IATA 3-letter domain</text>
    <text x="56" y="278" font-size="11">Largest. First. Non-negotiable.</text>

    <rect x="236" y="84" width="180" height="220" fill="{PAPER}" stroke="{INK}" stroke-width="1.5"/>
    <text x="252" y="112" font-size="12" font-weight="700" letter-spacing="2">2 SECONDARY</text>
    <text x="252" y="168" font-family="ui-monospace, Courier New, monospace" font-size="16">{LPN}</text>
    <text x="252" y="220" font-size="11">LPN + dual barcodes</text>
    <text x="252" y="240" font-size="11">10-digit machine key</text>
    <text x="252" y="278" font-size="11">Readable if type fails.</text>

    <rect x="432" y="84" width="160" height="220" fill="{PAPER}" stroke="{INK}" stroke-width="1.25"/>
    <text x="448" y="112" font-size="12" font-weight="700" letter-spacing="2">3 CONTEXT</text>
    <text x="448" y="168" font-family="ui-monospace, Courier New, monospace" font-size="14">TG 676</text>
    <text x="448" y="188" font-size="12">08SEP26</text>
    <text x="448" y="220" font-size="11">Carrier · flight · date</text>
    <text x="448" y="278" font-size="11">Sort without a lookup.</text>

    <rect x="608" y="84" width="160" height="220" fill="{PAPER}" stroke="{INK}" stroke-width="1.25"/>
    <text x="624" y="112" font-size="12" font-weight="700" letter-spacing="2">4 FALLBACK</text>
    <text x="624" y="168" font-size="14" font-weight="700">ARKARA/NON</text>
    <text x="624" y="220" font-size="11">Passenger name</text>
    <text x="624" y="278" font-size="11">When machines fail.</text>

    <rect x="784" y="84" width="156" height="220" fill="{PAPER}" stroke="{INK}" stroke-width="1"/>
    <text x="800" y="112" font-size="12" font-weight="700" letter-spacing="2">5 BACKUP</text>
    <text x="800" y="168" font-size="14" font-weight="700">CLAIM</text>
    <text x="800" y="188" font-size="12">STUB · STUB</text>
    <text x="800" y="220" font-size="11">Same identity, torn off</text>
    <text x="800" y="278" font-size="11">Absence loses the bag.</text>
  </g>

  <text x="40" y="344" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="700" fill="{INK}">THEN, ALWAYS ON</text>
  <text x="40" y="368" font-family="Arial, Helvetica, sans-serif" font-size="13" fill="{INK}">Machine-readability (dual encoding)  →  material durability  →  sustainability lifecycle</text>
  <text x="40" y="396" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="{INK}">Size is hierarchy. Domain is meaning. Neither is decoration.</text>
</svg>
'''
    write(DIAG / "human-scan-hierarchy.svg", svg)


def po_gate() -> None:
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 520" role="img" aria-labelledby="title">
  <title id="title">PO Completeness gate — every element must earn its place</title>
  <rect width="980" height="520" fill="{GROUND}"/>
  <text x="40" y="36" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="700" letter-spacing="2" fill="{INK}">PO COMPLETENESS GATE · ประตูความครบ</text>
  <text x="40" y="58" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="{INK}">Closed package: if an element is present, it is required. If it is required, its absence breaks the system.</text>

  <g font-family="Arial, Helvetica, sans-serif" fill="{INK}" stroke="{INK}">
    <rect x="40" y="88" width="200" height="64" fill="{PAPER}" stroke-width="1.5"/>
    <text x="56" y="116" font-size="13" font-weight="700" stroke="none">ELEMENT ARRIVES</text>
    <text x="56" y="136" font-size="11" stroke="none">type, colour, rule, icon, copy</text>

    <polygon points="240,120 268,120 268,112 292,128 268,144 268,136 240,136" fill="{INK}" stroke="none"/>

    <rect x="300" y="88" width="200" height="64" fill="{PAPER}" stroke-width="1.5"/>
    <text x="316" y="116" font-size="13" font-weight="700" stroke="none">EXPLICIT MEANING?</text>
    <text x="316" y="136" font-size="11" stroke="none">Can you name the domain?</text>

    <polygon points="500,120 528,120 528,112 552,128 528,144 528,136 500,136" fill="{INK}" stroke="none"/>

    <rect x="560" y="88" width="200" height="64" fill="{PAPER}" stroke-width="1.5"/>
    <text x="576" y="116" font-size="13" font-weight="700" stroke="none">NON-REDUNDANT?</text>
    <text x="576" y="136" font-size="11" stroke="none">Does another element already say it?</text>

    <polygon points="760,120 788,120 788,112 812,128 788,144 788,136 760,136" fill="{INK}" stroke="none"/>

    <rect x="740" y="188" width="200" height="64" fill="{PAPER}" stroke-width="2"/>
    <text x="756" y="216" font-size="13" font-weight="700" stroke="none">SIZE + DOMAIN SET?</text>
    <text x="756" y="236" font-size="11" stroke="none">Weight matches scan order.</text>
  </g>

  <!-- fail / pass -->
  <g font-family="Arial, Helvetica, sans-serif" fill="{INK}">
    <line x1="400" y1="152" x2="400" y2="220" stroke="{INK}" stroke-width="1.5"/>
    <rect x="300" y="220" width="200" height="56" fill="#111111"/>
    <text x="316" y="244" font-size="13" font-weight="700" fill="{PAPER}">FAIL — REMOVE</text>
    <text x="316" y="262" font-size="11" fill="{PAPER}">Decorative / filler / slogan</text>

    <line x1="660" y1="152" x2="660" y2="220" stroke="{INK}" stroke-width="1.5"/>
    <rect x="560" y="220" width="200" height="56" fill="#111111"/>
    <text x="576" y="244" font-size="13" font-weight="700" fill="{PAPER}">FAIL — MERGE</text>
    <text x="576" y="262" font-size="11" fill="{PAPER}">Said twice, keep the stronger</text>

    <line x1="840" y1="252" x2="840" y2="300" stroke="{INK}" stroke-width="1.5"/>
    <rect x="740" y="300" width="200" height="56" fill="#111111"/>
    <text x="756" y="324" font-size="13" font-weight="700" fill="{PAPER}">FAIL — RESIZE</text>
    <text x="756" y="342" font-size="11" fill="{PAPER}">Wrong weight for the domain</text>

    <rect x="40" y="300" width="460" height="80" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>
    <text x="56" y="332" font-size="16" font-weight="700">PASS — KEEP</text>
    <text x="56" y="356" font-size="12">Present because required. Required because absence would break routing, claim, or audit.</text>
  </g>

  <text x="40" y="424" font-family="Arial, Helvetica, sans-serif" font-size="13" font-weight="700" fill="{INK}">OPTIONAL IS NOT A CATEGORY</text>
  <text x="40" y="448" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="{INK}">RFID, colour, and sustainability marks enter only when the domain is in the package (priority, crew, hazard, reusable, cold-chain).</text>
  <text x="40" y="476" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="{INK}">Motivational copy, empty badges, and “eco” ornaments fail the gate by default.</text>
</svg>
'''
    write(DIAG / "po-completeness-gate.svg", svg)


def mapping() -> None:
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 520" role="img" aria-labelledby="title">
  <title id="title">Baggage tag zones mapped onto website and dashboard surfaces</title>
  <rect width="980" height="520" fill="{GROUND}"/>
  <text x="40" y="36" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="700" letter-spacing="2" fill="{INK}">TAG → INTERFACE MAP · จากป้ายสู่จอ</text>
  <text x="40" y="58" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="{INK}">Same hierarchy. Different substrate. Do not invent a second visual language.</text>

  <g font-family="Arial, Helvetica, sans-serif" fill="{INK}">
    <text x="40" y="92" font-size="12" font-weight="700" letter-spacing="2">PHYSICAL TAG</text>
    <text x="520" y="92" font-size="12" font-weight="700" letter-spacing="2">WEBSITE / DASHBOARD / DOC / LOG</text>

    <rect x="40" y="108" width="200" height="52" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>
    <text x="52" y="132" font-size="20" font-weight="800">BKK</text>
    <text x="52" y="150" font-size="10">DestinationHero</text>
    <path d="M250 134 H500" stroke="{INK}" stroke-width="1.25" marker-end="url(#arr)"/>
    <rect x="520" y="108" width="420" height="52" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>
    <text x="536" y="132" font-size="16" font-weight="800">Page title · route · status noun</text>
    <text x="536" y="150" font-size="11">The one fact a stressed human must get in &lt;1 s</text>

    <rect x="40" y="176" width="200" height="52" fill="{PAPER}" stroke="{INK}" stroke-width="1.5"/>
    <text x="52" y="198" font-family="ui-monospace, Courier New, monospace" font-size="12">{LPN}</text>
    <text x="52" y="216" font-size="10">IdBlock + barcode</text>
    <path d="M250 202 H500" stroke="{INK}" stroke-width="1.25"/>
    <rect x="520" y="176" width="420" height="52" fill="{PAPER}" stroke="{INK}" stroke-width="1.5"/>
    <text x="536" y="198" font-size="13" font-weight="700">Stable ID · request id · object key</text>
    <text x="536" y="216" font-size="11">Monospace. Copyable. Dual-encoded (human + machine)</text>

    <rect x="40" y="244" width="200" height="52" fill="{PAPER}" stroke="{INK}" stroke-width="1.25"/>
    <text x="52" y="266" font-size="12">TG 676 · 08SEP26</text>
    <text x="52" y="284" font-size="10">StatusStrip</text>
    <path d="M250 270 H500" stroke="{INK}" stroke-width="1.25"/>
    <rect x="520" y="244" width="420" height="52" fill="{PAPER}" stroke="{INK}" stroke-width="1.25"/>
    <text x="536" y="266" font-size="13" font-weight="700">Owner · timestamp · environment</text>
    <text x="536" y="284" font-size="11">Enough to act without opening another pane</text>

    <rect x="40" y="312" width="200" height="52" fill="{PAPER}" stroke="{INK}" stroke-width="1.25"/>
    <text x="52" y="334" font-size="12">ARKARA/NON</text>
    <text x="52" y="352" font-size="10">Fallback line</text>
    <path d="M250 338 H500" stroke="{INK}" stroke-width="1.25"/>
    <rect x="520" y="312" width="420" height="52" fill="{PAPER}" stroke="{INK}" stroke-width="1.25"/>
    <text x="536" y="334" font-size="13" font-weight="700">Human-readable subject</text>
    <text x="536" y="352" font-size="11">Name, title, or summary if IDs are unreadable</text>

    <rect x="40" y="380" width="200" height="52" fill="{PAPER}" stroke="{INK}" stroke-width="1"/>
    <text x="52" y="402" font-size="12">CLAIM · STUB</text>
    <text x="52" y="420" font-size="10">StubBackup</text>
    <path d="M250 406 H500" stroke="{INK}" stroke-width="1.25"/>
    <rect x="520" y="380" width="420" height="52" fill="{PAPER}" stroke="{INK}" stroke-width="1"/>
    <text x="536" y="402" font-size="13" font-weight="700">Receipt · permalink · export · audit</text>
    <text x="536" y="420" font-size="11">A copy that still identifies the object offline</text>
  </g>
  <text x="40" y="468" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="{INK}">TagCard = the closed package on a site. Dashboard row = the same package at list density. Log line = the same package at one line.</text>
  <text x="40" y="492" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="{INK}">Do not add a hero slogan. The destination *is* the hero.</text>
</svg>
'''
    write(DIAG / "website-dashboard-mapping.svg", svg)


def evolution() -> None:
    rows = [
        ("1", "THERMAL PAPER", "Short-haul, controlled indoor. Cheapest substrate. Print fades; moisture fails it."),
        ("2", "SYNTHETIC", "Long-haul / humid. Waterproof, abrasion-resistant facestock. Same print, harder life."),
        ("3", "PP / PE LAMINATE", "Most common durable loop tag. Film over thermal coat. Tear and scuff domain."),
        ("4", "FREEZER-GRADE", "Cold-chain / winter tarmac. Adhesive is the information: it must hold below freezing."),
        ("5", "RFID INLAY", "UHF EPC Gen2 / ISO 18000-6C (IATA RP1740C). Dual ID: barcode still present."),
        ("6", "EBT / REUSABLE", "Electronic / permanent tag (IATA RP1754). Lifecycle domain: reuse, battery, recycle."),
    ]
    blocks = []
    y = 96
    for n, title, body in rows:
        blocks.append(f'''
    <rect x="40" y="{y}" width="64" height="56" fill="{INK}"/>
    <text x="72" y="{y+36}" text-anchor="middle" font-size="18" font-weight="700" fill="{PAPER}">{n}</text>
    <rect x="104" y="{y}" width="836" height="56" fill="{PAPER}" stroke="{INK}" stroke-width="1.25"/>
    <text x="124" y="{y+24}" font-size="14" font-weight="700">{title}</text>
    <text x="124" y="{y+44}" font-size="12">{body}</text>''')
        y += 64
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 560" role="img" aria-labelledby="title">
  <title id="title">Evolutionary stack from thermal paper to reusable electronic tags</title>
  <rect width="980" height="560" fill="{GROUND}"/>
  <text x="40" y="36" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="700" letter-spacing="2" fill="{INK}">EVOLUTIONARY STACK · ชั้นวิวัฒนาการ</text>
  <text x="40" y="58" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="{INK}">Later layers add a domain. They do not delete earlier ones until the whole network can read them.</text>
  <g font-family="Arial, Helvetica, sans-serif" fill="{INK}">
    {''.join(blocks)}
  </g>
  <text x="40" y="500" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="{INK}">Vanhoenacker (2012): RFID cannot replace the printed ABT until most airports can handle it — dual encoding is the migration rule.</text>
  <text x="40" y="524" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="{INK}">Sustainability is a functional domain (reuse cycles, recycle plan, no-residue adhesive), not an eco ornament.</text>
</svg>
'''
    write(DIAG / "evolutionary-stack.svg", svg)


def portrait_tag() -> None:
    bars, _ = barcode_svg_rects(LPN, 28, 268, 56, module=0.78)
    vbars, _ = barcode_vertical_rects(LPN, 14, 48, 10, module=0.5)
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 640" role="img" aria-labelledby="title">
  <title id="title">Portrait thermal bag tag, example BKK / {LPN}</title>
  <rect width="280" height="640" fill="{GROUND}"/>
  <rect x="8" y="8" width="264" height="624" fill="{PAPER}" stroke="{INK}" stroke-width="2"/>
  <circle cx="140" cy="36" r="14" fill="none" stroke="{INK}" stroke-width="2"/>
  <circle cx="140" cy="36" r="5" fill="{GROUND}"/>
  <line x1="24" y1="60" x2="256" y2="60" stroke="{INK}" stroke-width="1" stroke-dasharray="3 4"/>
  {vbars}
  <text x="32" y="150" font-family="Arial Narrow, Arial, Helvetica, sans-serif" font-size="92" font-weight="800" letter-spacing="-4" fill="{INK}">BKK</text>
  <text x="34" y="176" font-family="Arial, Helvetica, sans-serif" font-size="11" letter-spacing="3" fill="{INK}">BANGKOK · จุดหมาย</text>
  <text x="34" y="208" font-family="ui-monospace, Courier New, monospace" font-size="13" fill="{INK}">TG 676</text>
  <text x="34" y="228" font-family="ui-monospace, Courier New, monospace" font-size="13" fill="{INK}">08SEP26  NRT–BKK</text>
  <text x="34" y="256" font-family="Arial, Helvetica, sans-serif" font-size="13" font-weight="700" letter-spacing="1.4" fill="{INK}">ARKARA/NON</text>
  {bars}
  <text x="28" y="344" font-family="ui-monospace, Courier New, monospace" font-size="14" letter-spacing="1.2" fill="{INK}">{LPN}</text>
  <g fill="none" stroke="{INK}" stroke-width="1.25">
    <rect x="28" y="372" width="224" height="64"/>
    <rect x="28" y="448" width="224" height="64"/>
    <rect x="28" y="524" width="224" height="72"/>
  </g>
  <text x="40" y="396" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="700" fill="{INK}">CLAIM / ใบรับกระเป๋า</text>
  <text x="40" y="418" font-family="ui-monospace, Courier New, monospace" font-size="12" fill="{INK}">{LPN}</text>
  <text x="40" y="472" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="700" fill="{INK}">STUB · LOAD</text>
  <text x="40" y="494" font-family="ui-monospace, Courier New, monospace" font-size="12" fill="{INK}">{LPN}</text>
  <text x="40" y="548" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="700" fill="{INK}">STUB · TRANSFER</text>
  <text x="40" y="570" font-family="ui-monospace, Courier New, monospace" font-size="12" fill="{INK}">{LPN}</text>
  <text x="40" y="614" font-family="Arial, Helvetica, sans-serif" font-size="9" letter-spacing="1" fill="{INK}">EXAMPLE · NOT A LIVE BAG</text>
</svg>
'''
    write(ASSETS / "tag-portrait.svg", svg)


if __name__ == "__main__":
    # sanity: checksum
    vals = code128_c_values(LPN)
    assert vals[-1] == 106
    # Retired 2026-09-09: hero(), anatomy(), hierarchy(), po_gate() and
    # mapping() are superseded by the illustrated WebP set in assets/. Their
    # generator functions are kept for reference and for the barcode geometry
    # they share, but running them would resurrect the replaced SVGs.
    mark()
    portrait_tag()
    evolution()
    print("LPN", LPN, "code128c", vals)
