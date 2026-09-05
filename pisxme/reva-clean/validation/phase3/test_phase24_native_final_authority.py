"""Focused Phase 24 native authority regression."""

from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    assert (ROOT / "PiSXMe_RevA_Clean_complete.kicad_sym").exists()
    assert '(uri "${KIPRJMOD}/PiSXMe_RevA_Clean_complete.kicad_sym")' in (
        ROOT / "sym-lib-table"
    ).read_text()
    root = (ROOT / "PiSXMe_RevA_Clean.kicad_sch").read_text()
    assert root.count('(global_label "') >= 60
    assert root.count('(sheet_instances (path "/" (page "1")))') == 1
    assert "c0000000-0000-0000-0000-000000000320" not in root
    assert "(wire (pts (xy 25 47) (xy 35 47))" in root
    child = (ROOT / "CORE_CM5.kicad_sch").read_text()
    assert child.count("MIPI1_D2_N") >= 1 and child.count("MIPI1_D2_P") >= 1
    with tempfile.TemporaryDirectory(prefix="pisxme-phase24-erc-"):
        report = ROOT / ".phase24-test-erc.rpt"
        result = subprocess.run(
            ["kicad-cli", "sch", "erc", "--severity-error",
             "--output", report.name, str(ROOT / "PiSXMe_RevA_Clean.kicad_sch")],
            cwd=ROOT, check=False,
        )
        assert result.returncode == 0, report.read_text() if report.exists() else result
        assert "; error" not in report.read_text()
        report.unlink(missing_ok=True)
    print("Phase 24 native final authority: PASS")


if __name__ == "__main__":
    main()
