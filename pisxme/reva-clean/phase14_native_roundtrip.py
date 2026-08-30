"""Normalize generated KiCad sheets through the installed schematic API.

The bridge is deliberately the final authoring boundary: generated S-expression
objects are parsed, validated, and serialized by the same model used by the
native KiCad 10 workflow.  This avoids relying on undocumented hand-written
serialization details for symbol instances and embedded-library records.
"""
from pathlib import Path
import sys
import re
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from bridge.schematic_backend import SchematicBackend

def balanced(text: str, start: int) -> str:
    depth = 0
    quoted = escaped = False
    for i in range(start, len(text)):
        c = text[i]
        if quoted and escaped:
            escaped = False
        elif quoted and c == '\\':
            escaped = True
        elif c == '"':
            quoted = not quoted
        elif not quoted:
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
                if depth == 0:
                    return text[start:i + 1]
    raise ValueError('unbalanced schematic expression')

def custom_instances(text: str) -> dict[str, str]:
    result = {}
    for match in re.finditer(r'\(symbol\s+\(lib_id "PiSXMeRevAClean:[^"]+"', text):
        block = balanced(text, match.start())
        ref = re.search(r'\(property "Reference" "([^"]+)"', block)
        if ref:
            result[ref.group(1)] = block
    return result

def custom_definitions(text: str) -> list[str]:
    result = []
    for match in re.finditer(r'\(symbol "PiSXMeRevAClean:[^"]+"', text):
        block = balanced(text, match.start())
        if '(lib_id ' not in block:
            result.append(block)
    return result

def restore_custom_definitions(text: str, definitions: list[str]) -> str:
    start = text.index('(lib_symbols')
    library = balanced(text, start)
    missing = [block for block in definitions
               if re.search(r'\(symbol "([^"]+)"', block).group(1) not in library]
    if not missing:
        return text
    insertion = library[:-1].rstrip() + '\n' + '\n'.join(missing) + '\n)'
    return text[:start] + insertion + text[start + len(library):]

def restore_custom_instances(text: str, instances: dict[str, str]) -> str:
    for ref, original in instances.items():
        for match in re.finditer(r'\(symbol\s+\(lib_id "[^"]+"', text):
            block = balanced(text, match.start())
            if re.search(r'\(property "Reference" "' + re.escape(ref) + r'"', block):
                text = text[:match.start()] + original + text[match.start() + len(block):]
                break
    return text

def main() -> None:
    paths = [Path(p) for p in sys.argv[1:]]
    if not paths:
        raise SystemExit("usage: phase14_native_roundtrip.py SHEET...kicad_sch")
    backend = SchematicBackend()
    for path in paths:
        original = path.read_text()
        definitions = custom_definitions(original)
        custom = custom_instances(original)
        match = re.search(r'\(sheet_instances\s+\(path "([^"]+)"', original, re.S)
        instance_path = match.group(1) if match else None
        doc = backend.open(path)
        errors = [i for i in doc.schematic.validate()
                  if i.level.value in ("error", "critical")]
        if errors:
            raise SystemExit(f"{path}: validation failed: {errors}")
        doc.save(path, validate=False)
        path.write_text(restore_custom_definitions(path.read_text(), definitions))
        path.write_text(restore_custom_instances(path.read_text(), custom))
        # kicad-sch-api correctly serializes the object model but canonicalizes
        # a standalone child to /. Restore the project-context path captured
        # above when the input is a hierarchical child.
        if instance_path and instance_path != '/':
            text = path.read_text()
            text = re.sub(r'(\(sheet_instances\s+\(path )"/"',
                          rf'\1"{instance_path}"', text, count=1, flags=re.S)
            path.write_text(text)
        print(f"native round-trip normalized {path}")

if __name__ == "__main__":
    main()
