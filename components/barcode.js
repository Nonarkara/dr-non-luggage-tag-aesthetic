/* SPDX-License-Identifier: MIT */
/* Code 128 encoder → SVG. No dependencies.
 *
 * Why this exists: v2 drew barcodes with a repeating-linear-gradient. That is a
 * picture of a barcode. The whole argument of this aesthetic is that the marks
 * are load-bearing — that the strip really does carry the data that moves the
 * object. A decorative barcode quietly concedes the opposite, and once you have
 * conceded it the rest of the system is only styling.
 *
 * These render as genuinely scannable symbols. Point a phone at one.
 *
 * Set C is the default for all-numeric, even-length payloads: it packs two
 * digits into each 11-module symbol. That compression is the reason the IATA
 * licence plate is a 10-digit number and not a string — the format was chosen
 * to fit the barcode, not the other way round.
 */

// Code 128 element widths. Six elements per symbol (bar,space,bar,space,bar,space),
// widths 1–4 modules. Index = symbol value. 106 is STOP and has seven elements.
const PATTERNS = [
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

const START_B = 104;
const START_C = 105;
const STOP = 106;

const isNumericPair = (value) => /^\d+$/.test(value) && value.length % 2 === 0;

/**
 * Convert a payload into Code 128 symbol values, including start and checksum.
 * @param {string} value
 * @returns {number[]}
 */
function encodeSymbols(value) {
  const symbols = [];

  if (isNumericPair(value)) {
    symbols.push(START_C);
    for (let i = 0; i < value.length; i += 2) {
      symbols.push(Number(value.slice(i, i + 2)));
    }
  } else {
    symbols.push(START_B);
    for (const char of value) {
      const code = char.charCodeAt(0);
      if (code < 32 || code > 126) {
        throw new RangeError(`Code 128 Set B cannot encode ${JSON.stringify(char)}`);
      }
      symbols.push(code - 32);
    }
  }

  // Modulo-103 weighted checksum. Start symbol has weight 1, then 1,2,3...
  const checksum = symbols.reduce(
    (sum, symbol, index) => sum + symbol * (index === 0 ? 1 : index),
    0
  ) % 103;

  symbols.push(checksum, STOP);
  return symbols;
}

/**
 * Build the run-length bar/space sequence for a payload.
 * @param {string} value
 * @returns {{widths: number[], modules: number}} alternating bar,space,bar... widths
 */
export function encode(value) {
  const widths = encodeSymbols(value)
    .flatMap((symbol) => PATTERNS[symbol].split('').map(Number));
  const modules = widths.reduce((total, width) => total + width, 0);
  return { widths, modules };
}

/**
 * Render a scannable Code 128 symbol as an SVG string.
 *
 * @param {string} value payload
 * @param {object} [options]
 * @param {number} [options.module=2]  narrow-element width in px
 * @param {number} [options.height=72] bar height in px
 * @param {number} [options.quiet=10]  quiet zone in modules (spec minimum is 10)
 * @param {string} [options.ink='#111111']
 * @returns {string} SVG markup
 */
export function toSVG(value, options = {}) {
  const {
    module = 2,
    height = 72,
    quiet = 10,
    ink = '#111111'
  } = options;

  const { widths, modules } = encode(value);
  const width = (modules + quiet * 2) * module;

  // Even indices are bars, odd are spaces.
  let cursor = quiet * module;
  const rects = [];
  widths.forEach((runLength, index) => {
    const runWidth = runLength * module;
    if (index % 2 === 0) {
      rects.push(`<rect x="${cursor}" y="0" width="${runWidth}" height="${height}"/>`);
    }
    cursor += runWidth;
  });

  return [
    `<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}"`,
    ` viewBox="0 0 ${width} ${height}" role="img"`,
    ` aria-label="Code 128 barcode, value ${value}" fill="${ink}"`,
    ' shape-rendering="crispEdges">',
    `<rect width="${width}" height="${height}" fill="none"/>`,
    rects.join(''),
    '</svg>'
  ].join('');
}

/**
 * Replace every [data-barcode] element with a rendered symbol.
 * The element's data-barcode value is the payload.
 */
export function renderAll(root = document) {
  root.querySelectorAll('[data-barcode]').forEach((node) => {
    const value = node.dataset.barcode;
    if (!value) return;
    try {
      node.innerHTML = toSVG(value, {
        module: Number(node.dataset.barcodeModule) || 2,
        height: Number(node.dataset.barcodeHeight) || 72
      });
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
