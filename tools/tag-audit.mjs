#!/usr/bin/env node
/**
 * tag-audit — the PO Completeness gate, made runnable.
 *
 * `docs/critique-checklist.md` is the human gate. This is the machine half:
 * the subset of that checklist a computer can decide without judgment.
 *
 * It cannot tell you whether an element carries meaning. It can tell you that
 * a corner is rounded, that the id outranks the destination, that a colour
 * appears with no domain behind it, or that a banned typeface crept in.
 *
 * Usage:
 *   node tools/tag-audit.mjs [path] [--strict] [--json]
 *
 * Exit: 0 clean (or warnings only) · 1 errors found · 2 bad usage
 */

import { readdir, readFile, stat } from 'node:fs/promises';
import { join, relative, resolve, sep } from 'node:path';

const SCAN_EXT = ['.html', '.css', '.js', '.mjs', '.jsx', '.ts', '.tsx', '.svelte', '.vue'];
const SKIP = [/node_modules/, /\.git/, /dist/, /build/, /package-lock\.json$/, /tools\/tag-audit\.mjs$/];

/** Each rule: {re, msg, severity, note?}. `error` blocks ship; `warn` asks a human. */
const RULES = {
  // ── Material: the tag is a flat printed object ────────────────────────
  material: [
    { re: /border-radius\s*:\s*(?!\s)(?!0\b|50%|var\(--tag-radius\))[^;]+/g,
      msg: 'Rounded corner. A tag is die-cut, not a pill. --tag-radius is 0.' },
    { re: /borderRadius\s*:\s*['"](?!0|50%)/g,
      msg: 'Rounded corner (JS style). --tag-radius is 0.' },
    { re: /box-shadow\s*:(?![^;]*inset)[^;]*[1-9]/g,
      msg: 'Drop shadow. Printed ink casts none. Use a rule, not elevation.' },
    { re: /(?<!repeating-)(linear|radial|conic)-gradient\s*\(/g,
      msg: 'Gradient. Thermal print is one ink on one ground.' },
    { re: /repeating-(linear|radial)-gradient\s*\(/g,
      msg: 'Repeating gradient. Legitimate only when it renders a machine symbol (barcode bars). Decorative stripes fail PO.',
      severity: 'warn' },
    { re: /backdrop-filter\s*:|filter\s*:[^;]*blur\s*\(/g,
      msg: 'Blur / glassmorphism. Checklist (f): do not invert the tag into a dark glass card.' },
  ],

  // ── Type: four ranks, and the object is not a template ───────────────
  type: [
    { re: /['"](Inter|Roboto|Poppins|Montserrat|Open Sans|Lato|Geist|Space Grotesk|Manrope|DM Sans)['"]/g,
      msg: 'Banned template typeface. Recognisable as machine output; the tag uses a condensed grotesque.' },
    { re: /family=(Inter|Roboto|Poppins|Montserrat|Open\+Sans|Lato|Geist|Space\+Grotesk)\b/g,
      msg: 'Banned template typeface in a font URL.' },
    { re: /font-size\s*:\s*(?!var\(--tag-)[0-9.]+(px|rem|em)/g,
      msg: 'Off-token font-size. Size is information — it comes from a rank token, not a number.',
      severity: 'warn' },
  ],

  // ── Colour: ground + ink. Colour is a domain, never a rank ───────────
  colour: [
    { re: /#(?:6366f1|818cf8|8b5cf6|a855f7|7c3aed|6d28d9|4f46e5)\b/gi,
      msg: 'Indigo/violet accent. The most-cited tell of generated design, and no domain owns it.' },
    { re: /#(?:3b82f6|2563eb|60a5fa)\b/gi,
      msg: 'Default framework blue. Not a domain colour.' },
    { re: /#(?:0{3}|0{6})\b/g,
      msg: 'Pure #000. Thermal ink is #111111 — pure black reads as unstyled, not as printed.',
      severity: 'warn' },
  ],

  // ── PO Completeness: noise the gate already forbids in prose ─────────
  noise: [
    { re: /(?:seamless(?:ly)?|cutting-edge|unlock the power|transform your|elevate your|supercharge|revolutionis|game-chang)\w*/gi,
      msg: 'Marketing sentence. Checklist (b): no filler, motivational, or marketing copy.' },
    { re: /(?:Welcome back|Get started in|Now in Beta|Powered by AI)/gi,
      msg: 'Filler chrome. No domain owns it.' },
    { re: /[\u{1F300}-\u{1FAFF}\u{2728}\u{2B50}\u{1F947}-\u{1F949}]/gu,
      msg: 'Emoji. Checklist (b): no emoji, sparkle, or "welcome back".' },
  ],
};

/** Rules that only make sense inside a rendered surface. */
const UI_ONLY = new Set(['noise']);
const UI_EXT = ['.html', '.jsx', '.tsx', '.svelte', '.vue'];

/**
 * Blank out comment spans so a rule never fires on prose describing that rule.
 * Padding preserves column numbers.
 */
function stripComments(line) {
  const pad = (m) => ' '.repeat(m.length);
  let out = line.replace(/\/\*[\s\S]*?\*\//g, pad).replace(/<!--[\s\S]*?-->/g, pad);
  if (/^\s*(?:\/\/|\/\*|\*|<!--)/.test(out)) return ' '.repeat(line.length);
  const s = out.search(/(?<!:)\/\//);
  return s === -1 ? out : out.slice(0, s) + ' '.repeat(out.length - s);
}

/**
 * Blank out `.tag-noise` regions.
 *
 * The examples are before/after demonstrations: the Before panel is SUPPOSED to
 * fail the gate. `.tag-noise` is the repo's existing vocabulary for that, so it
 * is reused here rather than inventing a second marker. Newlines are preserved
 * so reported line numbers stay true.
 */
function maskNoise(text, isUi) {
  const blank = (m) => m.replace(/[^\n]/g, ' ');
  let out = text.replace(/\.tag-noise[^{]*\{[^}]*\}/g, blank); // CSS rule blocks
  if (!isUi) return out;
  // Single elements declared as deliberate failures.
  out = out.replace(/<(\w+)[^>]*\bdata-po="fail"[^>]*>[\s\S]*?<\/\1>/g, blank);
  // HTML subtree: from the opening tag carrying tag-noise to its matching close.
  const open = /<(\w+)([^>]*\bclass="[^"]*\btag-noise\b[^"]*"[^>]*)>/g; // subtree form
  let m;
  while ((m = open.exec(out)) !== null) {
    const tag = m[1];
    let depth = 1, i = open.lastIndex;
    const step = new RegExp(`<${tag}\\b|</${tag}>`, 'g');
    step.lastIndex = i;
    let t;
    while (depth > 0 && (t = step.exec(out)) !== null) {
      depth += t[0].startsWith('</') ? -1 : 1;
      i = step.lastIndex;
    }
    out = out.slice(0, m.index) + blank(out.slice(m.index, i)) + out.slice(i);
    open.lastIndex = m.index;
  }
  return out;
}

async function collect(root) {
  const out = [];
  async function walk(dir) {
    let entries;
    try { entries = await readdir(dir, { withFileTypes: true }); } catch { return; }
    for (const e of entries) {
      const p = join(dir, e.name);
      if (SKIP.some((re) => re.test(relative(root, p)))) continue;
      if (e.isDirectory()) await walk(p);
      else if (SCAN_EXT.some((x) => p.endsWith(x))) out.push(p);
    }
  }
  const s = await stat(root).catch(() => null);
  if (!s) return [];
  if (s.isFile()) return SCAN_EXT.some((x) => root.endsWith(x)) ? [root] : [];
  await walk(root);
  return out;
}

/**
 * Hierarchy is the one rule that needs the whole file, not one line:
 * the id must never outrank the destination. That is a domain error.
 */
function checkHierarchy(text, rel) {
  const found = [];
  const sizeOf = (token) => {
    const m = text.match(new RegExp(`--tag-size-${token}\\s*:\\s*([^;]+);`));
    if (!m) return null;
    const rem = m[1].match(/([\d.]+)rem/);
    const clampMax = m[1].match(/clamp\([^,]+,[^,]+,\s*([\d.]+)rem/);
    return clampMax ? parseFloat(clampMax[1]) : rem ? parseFloat(rem[1]) : null;
  };
  const dest = sizeOf('dest'), lpn = sizeOf('lpn');
  if (dest !== null && lpn !== null && lpn >= dest) {
    found.push({
      file: rel, line: 1, col: 1, match: `lpn ${lpn}rem >= dest ${dest}rem`,
      msg: 'Inverted hierarchy: the id is not smaller than the destination. Size is information — this says the machine key outranks where the bag goes.',
      severity: 'error',
    });
  }
  return found;
}

/** A coloured element with no declared domain fails size–domain coherence (e). */
function checkDomainColour(text, rel) {
  const found = [];
  const re = /var\(--tag-domain-(priority|crew|hazard)\)/g;
  let m;
  while ((m = re.exec(text)) !== null) {
    const around = text.slice(Math.max(0, m.index - 400), m.index + 400);
    if (!/data-domain|\[data-domain|--tag-domain-mark/.test(around)) {
      found.push({
        file: rel, line: text.slice(0, m.index).split('\n').length, col: 1, match: m[0],
        msg: 'Domain colour with no data-domain nearby. Checklist (e): colour marks a domain that is in the record, never "energy".',
        severity: 'warn',
      });
    }
  }
  return found;
}

async function scanFile(file, root) {
  const rel = relative(root, file).split(sep).join('/');
  const raw = await readFile(file, 'utf8');
  const ui = UI_EXT.some((x) => file.endsWith(x));
  const text = maskNoise(raw, ui);
  const out = [];

  text.split(/\r?\n/).forEach((raw, i) => {
    if (/tag-audit-ignore/.test(raw)) return;
    const line = stripComments(raw);
    for (const [cat, rules] of Object.entries(RULES)) {
      if (UI_ONLY.has(cat) && !ui) continue;
      for (const r of rules) {
        r.re.lastIndex = 0;
        let m;
        while ((m = r.re.exec(line)) !== null) {
          out.push({ file: rel, line: i + 1, col: m.index + 1, match: m[0].slice(0, 60),
                     msg: r.msg, severity: r.severity ?? 'error' });
        }
      }
    }
  });

  out.push(...checkHierarchy(text, rel), ...checkDomainColour(text, rel));
  return out;
}

const args = process.argv.slice(2);
if (args.includes('-h') || args.includes('--help')) {
  console.log(`tag-audit — the machine half of the PO Completeness gate.

  node tools/tag-audit.mjs [path] [--strict] [--json]

  --strict  exit 1 on errors (CI)
  --json    machine-readable

It decides what a computer can decide. Meaning, non-redundancy, and whether an
element earns its place remain human questions — docs/critique-checklist.md.`);
  process.exit(0);
}
const json = args.includes('--json');
const root = resolve(process.cwd(), args.find((a) => !a.startsWith('--')) ?? '.');
const files = await collect(root);
const findings = (await Promise.all(files.map((f) => scanFile(f, root)))).flat();
const errors = findings.filter((f) => f.severity === 'error').length;
const warnings = findings.length - errors;

if (json) {
  console.log(JSON.stringify({ root, files: files.length, errors, warnings, findings }, null, 2));
} else {
  console.log(`tag-audit  ${files.length} files scanned · ${errors} error(s) · ${warnings} warning(s)\n`);
  let last = '';
  for (const f of findings.sort((a, b) => a.file.localeCompare(b.file) || a.line - b.line)) {
    if (f.file !== last) { console.log(`${f.file}`); last = f.file; }
    console.log(`  ${f.severity === 'error' ? '✗' : '!'} ${String(f.line).padStart(4)}:${String(f.col).padEnd(3)} ${f.msg}  \`${f.match}\``);
  }
  console.log(findings.length ? `\n${errors} error(s), ${warnings} warning(s).` : 'PO gate (machine half): clean.');
}
process.exit(errors > 0 ? 1 : 0);
