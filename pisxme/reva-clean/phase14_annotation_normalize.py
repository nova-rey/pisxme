"""Normalize generated instance references to KiCad-legal project references.

Human-readable block names remain in Value/MPN fields; references are the
machine-facing identifiers consumed by KiCad annotation and netlist export.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
REFERENCE_MAP = {
    "X_CORE_CM5": "X1", "X_V100_PCIE": "X2", "X_V100_POWER": "X3",
    "X_POWER_INPUT": "X4", "X_REGULATORS": "X5", "X_ETHERNET": "X6",
    "X_STORAGE": "X7", "X_SERVICE": "X8", "X_COOLING": "X9", "X_DEBUG": "X10",
    "J_V100": "J1", "C_PET0_P": "C1", "C_PET0_N": "C2",
    "U_PROTECT_A": "U1", "U_PROTECT_B": "U2", "U_CM5_5V": "U3",
    "U_BRIDGE_3V3": "U4", "U_BRIDGE_1V1": "U5", "J_ETHERNET": "J2",
    "U_ETH_ESD": "U6", "U_ETH_ESD_A": "U6", "U_ETH_ESD_B": "U9", "J_STORAGE_M2": "J3",
    "J_SERVICE": "J4", "U_SERVICE_ESD": "U8", "R_RD_A": "R1", "R_RD_B": "R2",
    "J_INPUT_A": "J5", "J_INPUT_B": "J6",
}

def main() -> None:
    changed = []
    for path in sorted(ROOT.glob("*.kicad_sch")):
        text = path.read_text()
        original = text
        for old, new in REFERENCE_MAP.items():
            text = re.sub(rf'(?<=property "Reference" "){re.escape(old)}(?=")', new, text)
            text = re.sub(rf'(?<=\(reference "){re.escape(old)}(?=")', new, text)
        if text != original:
            path.write_text(text)
            changed.append(path.name)
    print(f"Phase 14 annotation normalization: changed={','.join(changed) or 'none'}")

if __name__ == "__main__":
    main()
