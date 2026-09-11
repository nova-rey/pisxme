"""Disposable probe for repeated dangling REGULATORS wire stubs."""
from pathlib import Path
import sys
import re, shutil, subprocess

HERE=Path(__file__).resolve().parent
OUT=HERE/'.phase24_regulator_wire_probe'
CHILDREN=('CORE_CM5','V100_PCIE','V100_POWER','POWER_INPUT','REGULATORS','ETHERNET','STORAGE','SERVICE','COOLING','DEBUG')

def end(s,st):
 d=0;q=False;e=False
 for i in range(st,len(s)):
  c=s[i]
  if q and e:e=False
  elif q and c=='\\':e=True
  elif c=='"':q=not q
  elif not q and c=='(':d+=1
  elif not q and c==')':
   d-=1
   if d==0:return i+1
 raise ValueError(st)

if OUT.exists():shutil.rmtree(OUT)
OUT.mkdir()
files=['PiSXMe_RevA_Clean.kicad_sch','PiSXMe_RevA_Clean.kicad_pro',*[x+'.kicad_sch' for x in CHILDREN],'PiSXMe_RevA_Clean_complete.kicad_sym','Storage_DualMode.kicad_sym','sym-lib-table','fp-lib-table']
for f in files:shutil.copy2(HERE/f,OUT/f)
shutil.copytree(HERE/'PiSXMe_RevA_Clean.pretty',OUT/'PiSXMe_RevA_Clean.pretty')
p=OUT/'REGULATORS.kicad_sch';s=p.read_text();pos=0;spans=[]
while True:
 m=re.search(r'\(wire\s*\(pts\s*\(xy 70 ([0-9.+-]+)\)\s*\(xy 65 \1\)',s[pos:])
 if not m:break
 st=pos+m.start();spans.append((st,end(s,st)));pos=st+1
for a,b in reversed(spans):s=s[:a]+s[b:]
p.write_text(s);print(f'removed={len(spans)} output={OUT}')
report=OUT/'no-regulator-stubs-erc.rpt'
r=subprocess.run(['flatpak','run','--command=kicad-cli','org.kicad.KiCad','sch','erc','--severity-all','--output',str(report),str(OUT/'PiSXMe_RevA_Clean.kicad_sch')],cwd=OUT,text=True,capture_output=True)
print(r.stdout.strip());print(r.stderr.strip());print(f'erc_rc={r.returncode} report={report}')
if '--promote' in sys.argv:
    (HERE/'REGULATORS.kicad_sch').write_text(s)
    print('promoted=REGULATORS.kicad_sch')
