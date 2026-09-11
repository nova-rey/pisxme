"""Add only missing storage symbols to the canonical clean library.

The canonical library is authoritative for existing symbols.  Storage.kicad_sch
is the source of the reviewed storage definitions; this script deliberately
does not rebuild or replace any existing definition.
"""
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parent
TARGET = ROOT / "PiSXMe_RevA_Clean_complete.kicad_sym"
SOURCE = ROOT / "STORAGE.kicad_sch"
NAMES = (
    "JMS583_QFN64",
    "HD3SS6126_RUA0042A",
    "HD3SS3412_RUA0042A",
    "TE_1-2199230-4_MKEY",
    "STORAGE_MODE_BUFFER",
    "STORAGE_MODE_OVERRIDE",
    "STORAGE_PASSIVE_2",
    "STORAGE_CRYSTAL_4",
)


def block_end(text, start):
    depth = 0
    quoted = False
    escaped = False
    for i in range(start, len(text)):
        ch = text[i]
        if quoted:
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                quoted = False
            continue
        if ch == '"':
            quoted = True
        elif ch == '(':
            depth += 1
        elif ch == ')':
            depth -= 1
            if depth == 0:
                return i + 1
    raise ValueError(f"unbalanced S-expression at {start}")


def embedded_definition(text, name):
    needle = f'(symbol "PiSXMeRevAClean:{name}"'
    start = text.find(needle)
    if start < 0:
        raise ValueError(f"missing embedded definition: {name}")
    return text[start:block_end(text, start)]


def head_text():
    return subprocess.check_output(
        ["git", "show", f"HEAD:{TARGET.relative_to(ROOT.parent.parent)}"],
        text=True,
    )


def main():
    target = head_text()
    source = SOURCE.read_text()
    existing = set(re.findall(r'\(symbol "PiSXMeRevAClean:([^"]+)"', target))
    additions = [embedded_definition(source, name) for name in NAMES
                 if name not in existing]
    if len(additions) != len(NAMES):
        raise SystemExit("refusing to rewrite: one or more storage symbols already exist")
    close = target.rfind(")")
    TARGET.write_text(target[:close].rstrip() + "\n" +
                      "\n".join(additions) + "\n)\n")
    print(f"preserved HEAD library; added {len(additions)} storage symbols")


if __name__ == "__main__":
    main()
