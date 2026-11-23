// THE WORLD IN ONE DAY — entry program for make.fun news-image-20261123.
// Copies the pre-rendered front page (entry.png, drawn by draw.py) into the
// output directory the grader provides. No network, no dependencies: only
// the Node 22 standard library. Copying a fixed file is deterministic, so
// two runs always produce identical bytes.
//
// Run locally with:
//   MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "out";
const target = join(outDir, "entry.png");

mkdirSync(outDir, { recursive: true });
writeFileSync(target, readFileSync(join(here, "entry.png")));
