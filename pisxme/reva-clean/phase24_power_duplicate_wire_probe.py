"""Disposable Phase 24 probe for duplicate POWER_INPUT wire records."""
from pathlib import Path
import re, shutil, subprocess

HERE = Path(__file__).resolve().parent
OUT = HERE / ".phase24_power_duplicate_wire_probe"
CHILDREN = ("CORE_CM5", "V100_PCIE", "V100_POWER", "POWER_INPUT", "REGULATORS", "ETHERNET", "STORAGE", "SERVICE", "COOLING", "DEBUG")
TARGETS = ("41.25", "38.75", "81.25", "78.75")

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()
files = ["PiSXMe_RevA_Clean.kicad_sch", "PiSXMe_RevA_Clean.kicad_pro", *[x + ".kicad_sch" for x in CHILDREN], "PiSXMe_RevA_Clean_complete.kicad_sym", "Storage_DualMode.kicad_sym", "sym-lib-table", "fp-lib-table"]
for name in files:
    shutil.copy2(HERE / name, OUT / name)
shutil.copytree(HERE / "PiSXMe_RevA_Clean.pretty", OUT / "PiSXMe_RevA_Clean.pretty")

p = OUT / "POWER_INPUT.kicad_sch"
s = p.read_text()
removed = 0
for y in TARGETS:
    pat = re.compile(r"\(wire \(pts \(xy 70 " + re.escape(y) + r"\) \(xy 67 " + re.escape(y) + r"\)\) \(stroke \(width 0\) \(type default\)\) \(uuid [^)]+\)\)")
    m = pat.search(s)
    if m:
        s = s[:m.start()] + s[m.end():]
        removed += 1
p.write_text(s)
report = OUT / "power-duplicate-erc.rpt"
cmd = ["flatpak", "run", "--command=kicad-cli", "org.kicad.KiCad", "sch", "erc", "--severity-all", "--output", str(report), str(OUT / "PiSXMe_RevA_Clean.kicad_sch")]
r = subprocess.run(cmd, cwd=OUT, text=True, capture_output=True)
print(f"removed={removed} output={OUT}")
print(r.stdout.strip())
print(r.stderr.strip())
print(f"erc_rc={r.returncode} report={report}")
