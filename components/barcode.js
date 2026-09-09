/* SPDX-License-Identifier: MIT */
/* Barcode encoders → SVG. No dependencies.
 *
 * Why this exists: an earlier version drew barcodes with a
 * repeating-linear-gradient. That is a picture of a barcode. The whole argument
 * of this aesthetic is that the marks are load-bearing — that the strip really
 * does carry the data that moves the object. A decorative barcode quietly
 * concedes the opposite, and once you have conceded it the rest is styling.
 *
 * These render as genuinely scannable symbols. Point a phone at one.
 *
 * ── Symbology, and a correction ──────────────────────────────────────────
 * The interline bag tag licence plate is encoded in **Interleaved 2 of 5**,
 * not Code 128. IATA's Electronic Bag Tag Implementation Guide (§2.5) states
 * that baggage infrastructure is built on optically scanned interleaved 2 of 5,
 * that thousands of laser scanners read the 10-digit LPN, and that an EBT must
 * stay backward compatible by showing an interleaved 2 of 5 barcode of that
 * LPN — footnoting IATA R740 directly.
 *
 * This module previously used Code 128 and justified it with the observation
 * that Set C packs two digits per symbol. The observation was right; the
 * attribution was wrong. **I2of5 is the code that interleaves digit pairs** —
 * the first digit of each pair is carried in the bars, the second in the
 * spaces, which is why it needs an even digit count and why it fits ~10 digits
 * in roughly half the width of a non-interleaved symbol. A narrower symbol
 * allows a wider X dimension, which reads more reliably off a moving belt.
 *
 * So the "form follows encoding" point survives, and gets sharper: the LPN is a
 * 10-digit number partly because I2of5 wants an even count of numerals.
 *
 * Code 128 is retained for alphanumeric payloads (adjacent aviation uses), but
 * it is not what belongs under a destination code.
 */

/* ── Interleaved 2 of 5 ─────────────────────────────────────────────────── */

// Per digit, five elements, narrow(0) / wide(1).
const I25_DIGITS = [
  [0, 0, 1, 1, 0], // 0
  [1, 0, 0, 0, 1], // 1
  [0, 1, 0, 0, 1], // 2
  [1, 1, 0, 0, 0], // 3
  [0, 0, 1, 0, 1], // 4
  [1, 0, 1, 0, 0], // 5
  [0, 1, 1, 0, 0], // 6
  [0, 0, 0, 1, 1], // 7
  [1, 0, 0, 1, 0], // 8
  [0, 1, 0, 1, 0]  // 9
];

/**
 * Encode digits as Interleaved 2 of 5 run lengths.
 *
 * Digit pairs are interleaved: the first digit's five elements become bars,
 * the second digit's five become the spaces between them.
 *
 * @param {string} value even-length numeric string
 * @param {number} [wide=3] wide:narrow ratio (2 or 3; 3 is more robust)
 * @returns {{widths: number[], modules: number}} alternating bar,space widths
 */
export function encodeI25(value, wide = 3) {
  if (!/^\d+$/.test(value)) {
    throw new RangeError('Interleaved 2 of 5 encodes digits only');
  }
  if (value.length % 2 !== 0) {
    // Not a quirk to paper over: an odd count means this is not a licence
    // plate. Fail loudly rather than silently zero-padding a real id.
    throw new RangeError(
      `Interleaved 2 of 5 requires an even digit count; got ${value.length}`
    );
  }

  // Start: four narrow elements (bar space bar space).
  const widths = [1, 1, 1, 1];

  for (let i = 0; i < value.length; i += 2) {
    const bars = I25_DIGITS[Number(value[i])];
    const spaces = I25_DIGITS[Number(value[i + 1])];
    for (let e = 0; e < 5; e += 1) {
      widths.push(bars[e] ? wide : 1);
      widths.push(spaces[e] ? wide : 1);
    }
  }

  // Stop: wide bar, narrow space, narrow bar.
  widths.push(wide, 1, 1);

  return { widths, modules: widths.reduce((t, w) => t + w, 0) };
}

/* ── Code 128 (alphanumeric fallback) ───────────────────────────────────── */

const C128_PATTERNS = [
  '212222','222122','222221','121223','121322','131222','122213','122312','132212','221213',
  '221312','231212','112232','122132','122231','113222','123122','123221','223211','221132',
  '221231','213212','223112','312131','311222','321122','321221','312212','322112','322211',
  '212123','212321','232121','111323','131123','131321','112313','132113','132311','211313',
  '231113','231311','112133','112331','132131','113123','113321','133121','313121','211331',
  '231131','213113','213311','213131','311123','311321','331121','312113','312311','332111',
  '314111','221411','431111','111224','111422','121124','121421','141122','141221','112214',
  '112412','122114','122411','142112','142211','241211','221114','413111','241112','134111',
  '111242','121142','121241','114212','124112','124211','411212','421112','421211','212141',
  '214121','412121','111143','111341','131141','114113','114311','411113','411311','113141',
  '114131','311141','411131','211412','211214','211232','2331112'
];

/**
 * Encode an ASCII payload as Code 128 Set B run lengths.
 * @param {string} value
 * @returns {{widths: number[], modules: number}}
 */
export function encodeCode128(value) {
  const START_B = 104;
  const symbols = [START_B];

  for (const char of value) {
    const code = char.charCodeAt(0);
    if (code < 32 || code > 126) {
      throw new RangeError(`Code 128 Set B cannot encode ${JSON.stringify(char)}`);
    }
    symbols.push(code - 32);
  }

  const checksum = symbols.reduce(
    (sum, symbol, index) => sum + symbol * (index === 0 ? 1 : index),
    0
  ) % 103;

  symbols.push(checksum, 106 /* STOP */);

  const widths = symbols.flatMap((s) => C128_PATTERNS[s].split('').map(Number));
  return { widths, modules: widths.reduce((t, w) => t + w, 0) };
}

/**
 * Encode a payload, choosing the symbology the way a bag tag would:
 * Interleaved 2 of 5 for an even-length numeric licence plate, Code 128 only
 * when the payload is not a licence plate at all.
 *
 * @param {string} value
 * @param {'auto'|'i25'|'code128'} [symbology='auto']
 */
export function encode(value, symbology = 'auto') {
  if (symbology === 'i25') return encodeI25(value);
  if (symbology === 'code128') return encodeCode128(value);
  const isLicencePlate = /^\d+$/.test(value) && value.length % 2 === 0;
  return isLicencePlate ? encodeI25(value) : encodeCode128(value);
}

/* ── Render ─────────────────────────────────────────────────────────────── */

/**
 * Render a scannable symbol as an SVG string.
 *
 * @param {string} value payload
 * @param {object} [options]
 * @param {number} [options.module=2]  narrow-element width in px (X dimension)
 * @param {number} [options.height=72] bar height in px
 * @param {number} [options.quiet=10]  quiet zone in modules — 10 is the
 *                                     symbology minimum and IATA requires
 *                                     quiet zones be respected
 * @param {string} [options.ink='#111111']
 * @param {'auto'|'i25'|'code128'} [options.symbology='auto']
 * @returns {string} SVG markup
 */
export function toSVG(value, options = {}) {
  const {
    module = 2,
    height = 72,
    quiet = 10,
    ink = '#111111',
    symbology = 'auto'
  } = options;

  const { widths, modules } = encode(value, symbology);
  const width = (modules + quiet * 2) * module;

  let cursor = quiet * module;
  const rects = [];
  widths.forEach((runLength, index) => {
    const runWidth = runLength * module;
    if (index % 2 === 0) {
      rects.push(`<rect x="${cursor}" y="0" width="${runWidth}" height="${height}"/>`);
    }
    cursor += runWidth;
  });

  const label = symbology === 'code128' ? 'Code 128' : 'barcode';

  return [
    `<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}"`,
    ` viewBox="0 0 ${width} ${height}" role="img"`,
    ` aria-label="${label}, value ${value}" fill="${ink}"`,
    ' shape-rendering="crispEdges">',
    `<rect width="${width}" height="${height}" fill="none"/>`,
    rects.join(''),
    '</svg>'
  ].join('');
}

/**
 * Replace every [data-barcode] element with a rendered symbol.
 * `data-barcode` is the payload; `data-barcode-symbology` optionally forces one.
 */
export function renderAll(root = document) {
  root.querySelectorAll('[data-barcode]').forEach((node) => {
    const value = node.dataset.barcode;
    if (!value) return;
    try {
      node.innerHTML = toSVG(value, {
        module: Number(node.dataset.barcodeModule) || 2,
        height: Number(node.dataset.barcodeHeight) || 72,
        symbology: node.dataset.barcodeSymbology || 'auto'
      });
      node.removeAttribute('data-barcode-error');
    } catch (error) {
      // A tag that cannot encode its own id is a broken tag. Say so on the face
      // of the object rather than silently rendering a decorative smear.
      node.textContent = `BARCODE ERROR — ${error.message}`;
      node.setAttribute('data-barcode-error', 'true');
    }
  });
}

if (typeof document !== 'undefined') {
  const boot = () => renderAll();
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot, { once: true });
  } else {
    boot();
  }
}
