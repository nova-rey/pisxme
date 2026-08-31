"""Promote the eight Ethernet MDI boundary labels to native global nets.

The clean hierarchy intentionally keeps CORE_CM5 and ETHERNET as separate
sheets.  Their former aggregate CM5_GBE sheet pin could not express eight
independent pairs, so the named MDI boundaries are promoted in both sheets.
This is schematic authority, not a PCB net-name workaround.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
PAIRS = tuple(f"CM5_GBE_TD{i}_{pol}" for i in range(4) for pol in "PN")
LABEL_RE = re.compile(r'\(label "(CM5_GBE_TD[0-3]_[PN])"')


def promote(path: Path) -> int:
    text = path.read_text()
    before = len(LABEL_RE.findall(text))
    if before == 0 and all(f'(global_label "{name}"' in text for name in PAIRS):
        return 0
    for name in PAIRS:
        text = text.replace(f'(label "{name}"',
                            f'(global_label "{name}" (shape bidirectional)')
    after = len(LABEL_RE.findall(text))
    if before < 8:
        raise SystemExit(f"{path.name}: expected at least 8 local MDI labels, found {before}")
    if after:
        raise SystemExit(f"{path.name}: local MDI labels remain: {after}")
    path.write_text(text)
    return before


def main() -> None:
    changed = 0
    for name in ("CORE_CM5.kicad_sch", "ETHERNET.kicad_sch"):
        changed += promote(ROOT / name)
    print(f"Phase 17 Ethernet hierarchy authority: promoted {changed} MDI labels")


if __name__ == "__main__":
    main()
