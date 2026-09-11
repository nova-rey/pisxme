"""Promote the validated project-local PWR_FLAG namespace transformation."""
from pathlib import Path
import shutil

HERE=Path(__file__).resolve().parent
BACKUP=HERE/'.phase24_pwrflag_promotion_backup'
CH=('CORE_CM5','V100_PCIE','V100_POWER','POWER_INPUT','REGULATORS','ETHERNET','STORAGE','SERVICE','COOLING','DEBUG')
FILES=['PiSXMe_RevA_Clean.kicad_sch',*[x+'.kicad_sch' for x in CH],'PiSXMe_RevA_Clean_complete.kicad_sym']
if BACKUP.exists(): raise SystemExit('promotion backup exists; refusing overwrite')
BACKUP.mkdir()
for f in FILES: shutil.copy2(HERE/f,BACKUP/f)

def end(s,st):
 d=0;q=e=False
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

expr=None
for f in FILES[:-1]:
 p=HERE/f;s=p.read_text()
 if '(symbol "power:PWR_FLAG"' in s:
  st=s.index('(symbol "power:PWR_FLAG"'); en=end(s,st)
  if expr is None: expr=s[st:en].replace('(symbol "power:PWR_FLAG"','(symbol "PiSXMeRevAClean:PWR_FLAG"',1)
  s=s[:st]+expr+s[en:]
 s=s.replace('(lib_id "power:PWR_FLAG")','(lib_id "PiSXMeRevAClean:PWR_FLAG")')
 p.write_text(s)

lib=HERE/'PiSXMe_RevA_Clean_complete.kicad_sym'; s=lib.read_text()
if 'symbol "PiSXMeRevAClean:PWR_FLAG"' not in s:
 lib.write_text(s[:-2]+'\n'+expr+'\n)\n')
print('promoted project-local PWR_FLAG namespace; backup='+str(BACKUP))
