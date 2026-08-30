"""Add KiCad-native root sheet instance associations to the clean root."""
from pathlib import Path
from phase3_scaffold import SHEETS, balanced

ROOT = Path(__file__).resolve().parent
PATH = ROOT / "PiSXMe_RevA_Clean.kicad_sch"
ROOT_UUID = "30000000-0000-0000-0000-000000000000"

def main():
    text = PATH.read_text()
    cursor = 0
    blocks = []
    for page, name in enumerate(SHEETS, 1):
        marker = f'(property "Sheetname" "{name}"'
        prop = text.index(marker, cursor)
        start = text.rfind('(sheet', 0, prop)
        block = balanced(text, start)
        if '(instances' not in block:
            close = len(block) - 1
            association = f'''\n    (instances\n      (project "PiSXMe_RevA_Clean"\n        (path "/{ROOT_UUID}" (page "{page}"))\n      )\n    )'''
            block = block[:close] + association + block[close:]
        blocks.append((start, start + len(balanced(text, start)), block))
        cursor = start + len(block)
    for start, end, block in reversed(blocks):
        text = text[:start] + block + text[end:]
    PATH.write_text(text)
    print(f"root sheet associations applied: {len(blocks)}")

if __name__ == "__main__":
    main()
