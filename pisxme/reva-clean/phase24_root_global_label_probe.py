"""Disposable probe: remove one redundant root global label only."""
from pathlib import Path
import re, shutil, subprocess

HERE = Path(__file__).resolve().parent
OUT = HERE / ".phase24_root_global_label_probe"
CHILDREN = ("CORE_CM5", "V100_PCIE", "V100_POWER", "POWER_INPUT", "REGULATORS", "ETHERNET", "STORAGE", "SERVICE", "COOLING", "DEBUG")
if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir()
files = ["PiSXMe_RevA_Clean.kicad_sch", "PiSXMe_RevA_Clean.kicad_pro", *[x + ".kicad_sch" for x in CHILDREN], "PiSXMe_RevA_Clean_complete.kicad_sym", "Storage_DualMode.kicad_sym", "sym-lib-table", "fp-lib-table"]
for f in files: shutil.copy2(HERE / f, OUT / f)
shutil.copytree(HERE / "PiSXMe_RevA_Clean.pretty", OUT / "PiSXMe_RevA_Clean.pretty")
p = OUT / "PiSXMe_RevA_Clean.kicad_sch"
s = p.read_text()
pat = re.compile(r'  \(global_label "CM5_PER0_P".*?\n    \(uuid [^)]+\)\)', re.S)
m = pat.search(s)
if not m: raise SystemExit("target root global label not found")
s = s[:m.start()] + s[m.end():]
p.write_text(s)
report = OUT / "root-global-label-erc.rpt"
r = subprocess.run(["flatpak", "run", "--command=kicad-cli", "org.kicad.KiCad", "sch", "erc", "--severity-all", "--output", str(report), str(p)], cwd=OUT, text=True, capture_output=True)
print("removed=CM5_PER0_P root global label")
print(r.stdout.strip()); print(r.stderr.strip()); print(f"erc_rc={r.returncode} report={report}")
