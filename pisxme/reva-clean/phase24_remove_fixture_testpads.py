"""Create a disposable RTL9210B candidate without fixture-only test pads."""
from pathlib import Path

SRC = Path("PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_CRYSTAL_V3.kicad_pcb")
DST = Path("PHASE24_RTL9210B_FULL_LATERAL_SUPPORT_CRYSTAL_V4_NO_TESTPADS.kicad_pcb")
REFS = {f"TP{i}" for i in range(1, 9)}

def balanced_end(text: str, start: int) -> int:
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
        else:
            if ch == '"':
                quoted = True
            elif ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
                if depth == 0:
                    return i + 1
    raise ValueError("unbalanced KiCad object")

def remove_refs(text: str) -> str:
    pos = 0
    spans = []
    while True:
        start = text.find("(footprint ", pos)
        if start < 0:
            break
        end = balanced_end(text, start)
        block = text[start:end]
        if any(f"(property \"Reference\" \"{ref}\"" in block for ref in REFS):
            spans.append((start, end))
        pos = end
    for start, end in reversed(spans):
        text = text[:start] + text[end:]
    return text

data = remove_refs(SRC.read_text())
DST.write_text(data)
print(f"removed {len(REFS)} fixture references -> {DST}")
