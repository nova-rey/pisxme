"""Summarize native KiCad unconnected findings by serialized net."""
from collections import Counter
from pathlib import Path
import re

R = Path(__file__).resolve().parent
REPORT = R / "PHASE24_U5_INTEGRATED_LAYERED-drc.rpt"
OUT = R / "PHASE24_NATIVE_UNCONNECTED_CENSUS.md"
text = REPORT.read_text()
section = text[text.index("[unconnected_items]"):]
counts = Counter()
records = section.count("[unconnected_items]: Missing connection between items")
for block in section.split("[unconnected_items]: Missing connection between items")[1:]:
    # Each native item line has the form: Pad/PTH pad <n> [net] of ref.
    nets = re.findall(r"(?:Pad|PTH pad) [^\n]+? \[([^\]]*)\] of ", block[:700])
    if not nets:
        counts["<unparsed native record>"] += 1
        continue
    unique = list(dict.fromkeys(nets))
    counts[" <> ".join(unique)] += 1
lines = [
    "# Phase 24 native unconnected census",
    "",
    "Source: `PHASE24_U5_INTEGRATED_LAYERED-drc.rpt`; native DRC reported "
    f"{records} missing-connection records (each record has two endpoints).",
    "",
    "| Net or net pair | Native records |",
    "|---|---:|",
]
for net, count in counts.most_common():
    lines.append(f"| `{net or '<no net>'}` | {count} |")
lines += [
    "",
    "This is diagnostic evidence only. It does not waive native DRC or replace "
    "physical connectivity proof; every record remains a Phase 24 closure item.",
]
OUT.write_text("\n".join(lines) + "\n")
print(OUT)
