"""Regression for the TPSM63606 no-external-switch-node rule."""
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PYTHON = "/home/nyx/pisxme-toolchain-environment/bin/pisxme-pcbnew-python"


def main() -> None:
    result = subprocess.run([PYTHON, "validation/phase3/phase15_switch_containment_audit.py"],
                            cwd=ROOT, check=True, text=True, capture_output=True)
    assert "PASS" in result.stdout
    print(result.stdout.strip())


if __name__ == "__main__":
    main()
