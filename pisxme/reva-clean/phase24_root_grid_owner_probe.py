"""Disposable owner-aware root grid probe; canonical source is never edited."""
from pathlib import Path
import re, shutil, subprocess

HERE=Path(__file__).resolve().parent
OUT=HERE/'.phase24_root_grid_owner_probe'
CHILDREN=('CORE_CM5','V100_PCIE','V100_POWER','POWER_INPUT','REGULATORS','ETHERNET','STORAGE','SERVICE','COOLING','DEBUG')

def grid(v):
    return f'{round(float(v)/1.27)*1.27:g}'

if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir()
files=['PiSXMe_RevA_Clean.kicad_sch','PiSXMe_RevA_Clean.kicad_pro',*[x+'.kicad_sch' for x in CHILDREN],'PiSXMe_RevA_Clean_complete.kicad_sym','Storage_DualMode.kicad_sym','sym-lib-table','fp-lib-table']
for f in files: shutil.copy2(HERE/f,OUT/f)
shutil.copytree(HERE/'PiSXMe_RevA_Clean.pretty',OUT/'PiSXMe_RevA_Clean.pretty')
p=OUT/'PiSXMe_RevA_Clean.kicad_sch'; s=p.read_text()
def repl(m):
    return f'({m.group(1)} {grid(m.group(2))} {m.group(3)}'
s=re.sub(r'\((xy|at|start|end|position) ([0-9.+-]+) ([0-9.+-]+)',repl,s)
p.write_text(s)
print(f'root_coordinate_transform=all coordinate x fields to 1.27mm grid output={OUT}')
report=OUT/'root-grid-erc.rpt'
r=subprocess.run(['flatpak','run','--command=kicad-cli','org.kicad.KiCad','sch','erc','--severity-all','--output',str(report),str(p)],cwd=OUT,text=True,capture_output=True)
print(r.stdout.strip()); print(r.stderr.strip()); print(f'erc_rc={r.returncode} report={report}')
