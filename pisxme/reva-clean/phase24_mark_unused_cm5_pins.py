"""Mark unused CM5 MIPI pins as intentional no-connects for Rev A."""

from pathlib import Path
from uuid import UUID

ROOT = Path(__file__).resolve().parent
PATH = ROOT / "CORE_CM5.kicad_sch"
TARGETS = (("270.18", "155.88"), ("270.18", "158.42"))


def main() -> None:
    text = PATH.read_text()
    additions = []
    for index, (x, y) in enumerate(TARGETS):
        if f"(no_connect (at {x} {y})" not in text:
            additions.append(
                f'(no_connect (at {x} {y}) '
                f'(uuid {UUID(int=0xE4000000000000000000000000000000 + index)}))'
            )
    if additions:
        text = text.replace("\n)", "\n" + "\n".join(additions) + "\n)", 1)
        PATH.write_text(text)
    print(f"CM5 unused MIPI no-connects: {len(additions)}")


if __name__ == "__main__":
    main()
