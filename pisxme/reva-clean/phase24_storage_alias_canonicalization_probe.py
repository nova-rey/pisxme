"""Disposable probe for the two exact STORAGE alias canonicalizations."""
from pathlib import Path
import shutil,subprocess
R=Path(__file__).resolve().parent;OUT=R/'.phase24_storage_alias_canonicalization_probe_v3'
if OUT.exists():raise SystemExit('probe output exists; refusing overwrite')
OUT.mkdir();children=['CORE_CM5','V100_PCIE','V100_POWER','POWER_INPUT','REGULATORS','ETHERNET','STORAGE','SERVICE','COOLING','DEBUG']
for n in ['PiSXMe_RevA_Clean.kicad_sch','PiSXMe_RevA_Clean.kicad_pro','PiSXMe_RevA_Clean_complete.kicad_sym','Storage_DualMode.kicad_sym','sym-lib-table','fp-lib-table']+[x+'.kicad_sch' for x in children]:shutil.copy2(R/n,OUT/n)
shutil.copytree(R/'PiSXMe_RevA_Clean.pretty',OUT/'PiSXMe_RevA_Clean.pretty')
def records(s):
 i=0
 while True:
  i=s.find('(label "',i)
  if i<0:return
  j=i;depth=0;quote=False;esc=False
  while j<len(s):
   ch=s[j]
   if quote:
    if esc:esc=False
    elif ch=='\\':esc=True
    elif ch=='"':quote=False
   else:
    if ch=='"':quote=True
    elif ch=='(':depth+=1
    elif ch==')':
     depth-=1
     if depth==0:yield i,j+1,s[i:j+1];i=j+1;break
   j+=1
  else:return
p=OUT/'STORAGE.kicad_sch';s=p.read_text();changes=[('TME','POWER_GND','70 130.075'),('M2_CONFIG1','AUTO_PEDET','240 125.63')];done=[]
for start,end,rec in reversed(list(records(s))):
 for old,new,at in changes:
  if f'(label "{old}"' in rec and f'(at {at}' in rec:
   s=s[:start]+rec.replace(f'(label "{old}"',f'(label "{new}"',1)+s[end:];done.append((old,new,at));break
p.write_text(s);print('changes',done)
r=subprocess.run(['flatpak','run','--command=kicad-cli','org.kicad.KiCad','sch','erc','--severity-all','--output',str(OUT/'erc.rpt'),str(OUT/'PiSXMe_RevA_Clean.kicad_sch')],cwd=OUT,text=True,capture_output=True);print(r.stdout.strip());print(r.stderr.strip());print('erc_rc',r.returncode)
