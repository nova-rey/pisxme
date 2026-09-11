"""Disposable KiCad-10 installed-library probe for embedded PWR_FLAG."""
from pathlib import Path
import re, shutil, subprocess

HERE=Path(__file__).resolve().parent
OUT=HERE/'.phase24_pwrflag_library_probe'
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
root=OUT/'PiSXMe_RevA_Clean.kicad_sch'; s=root.read_text(); st=s.index('(symbol "power:PWR_FLAG"'); en=end(s,st)
lib=Path('/tmp/power-kicad10.kicad_sym').read_text(); lst=lib.index('(symbol "PWR_FLAG"'); len_=end(lib,lst); replacement=lib[lst:len_].replace('(symbol "PWR_FLAG"','(symbol "power:PWR_FLAG"',1)
root.write_text(s[:st]+replacement+s[en:])
report=OUT/'pwrflag-library-erc.rpt'
r=subprocess.run(['flatpak','run','--command=kicad-cli','org.kicad.KiCad','sch','erc','--severity-all','--output',str(report),str(root)],cwd=OUT,text=True,capture_output=True)
print(r.stdout.strip());print(r.stderr.strip());print(f'erc_rc={r.returncode} report={report}')
