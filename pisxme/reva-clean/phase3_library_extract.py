"""Extract approved CM5IO symbol definitions into the clean local namespace.

Only the named symbol definitions are copied; no schematic instances, donor
library tables, or machine-local paths are imported. The generated library is
an auditable Phase 3 input and is not a production connectivity claim by
itself.
"""

from pathlib import Path
import shutil

from phase3_scaffold import PORTS, contract_symbol

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "authority-inventory" / "cm5io-rev2" / "CM5IO.kicad_sym"
DEST = ROOT / "PiSXMe_RevA_Clean.kicad_sym"
FOOTPRINT_SOURCE = ROOT / "authority-inventory" / "cm5io-rev2" / "CM5IO.pretty" / "Raspberry-Pi-5-Compute-Module.kicad_mod"
FOOTPRINT_DEST = ROOT / "PiSXMe_RevA_Clean.pretty" / "PiSXMeRevAClean_Raspberry_Pi_5_Compute_Module.kicad_mod"
MODEL_SOURCE = ROOT / "authority-inventory" / "cm5io-rev2" / "CM5IO.3dshapes" / "10164227-1001a1rlf.stp"
MODEL_DEST = ROOT / "PiSXMe_RevA_Clean.3dshapes" / "10164227-1001a1rlf.stp"
SYMBOLS = ("ComputeModule5-CM5", "MagJack-A70-112-331N126")


def balanced(text: str, start: int) -> str:
    depth = 0
    quoted = False
    escaped = False
    for index in range(start, len(text)):
        char = text[index]
        if quoted and escaped:
            escaped = False
        elif quoted and char == "\\":
            escaped = True
        elif char == '"':
            quoted = not quoted
        elif not quoted:
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
                if depth == 0:
                    return text[start:index + 1]
    raise ValueError("unbalanced KiCad expression")


def extract(source: str, name: str) -> str:
    marker = f'(symbol "{name}"'
    start = source.index(marker)
    return balanced(source, start)


def main() -> None:
    source = SOURCE.read_text()
    definitions = []
    for name in SYMBOLS:
        definition = extract(source, name)
        definition = definition.replace(f'(symbol "{name}"',
                                        f'(symbol "PiSXMeRevAClean:{name}"', 1)
        definition = definition.replace(
            'CM5IO:Raspberry-Pi-5-Compute-Module',
            'PiSXMeRevAClean:PiSXMeRevAClean_Raspberry_Pi_5_Compute_Module',
        )
        definition = definition.replace(
            'CM5IO:TRJG0926HENL',
            'PiSXMeRevAClean:EDAC_A70_112_331N126',
        )
        definitions.append(definition)
    definitions.extend(contract_symbol(name, ports) for name, ports in PORTS.items())
    DEST.write_text(
        '(kicad_symbol_lib\n\t(version 20231120)\n'
        '\t(generator "PiSXMe Rev A Clean")\n'
        + "\n".join(definitions)
        + '\n)\n'
    )
    FOOTPRINT_DEST.parent.mkdir(exist_ok=True)
    footprint = FOOTPRINT_SOURCE.read_text()
    footprint = footprint.replace(
        '(footprint "Raspberry-Pi-5-Compute-Module"',
        '(footprint "PiSXMeRevAClean_Raspberry_Pi_5_Compute_Module"', 1)
    footprint = footprint.replace(
        '${KIPRJMOD}/CM5IO.3dshapes/10164227-1001a1rlf.stp',
        '${KIPRJMOD}/PiSXMe_RevA_Clean.3dshapes/10164227-1001a1rlf.stp',
    )
    FOOTPRINT_DEST.write_text(footprint)
    MODEL_DEST.parent.mkdir(exist_ok=True)
    shutil.copyfile(MODEL_SOURCE, MODEL_DEST)


if __name__ == "__main__":
    main()
