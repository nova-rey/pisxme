"""Disposable probe removing only x=70 duplicate NC label records."""
from pathlib import Path
import shutil,subprocess
R=Path(__file__).resolve().parent;OUT=R/'.phase24_storage_nc_exact_coordinate_probe'
if OUT.exists():raise SystemExit('probe output exists; refusing overwrite')
OUT.mkdir();children=['CORE_CM5','V100_PCIE','V100_POWER','POWER_INPUT','REGULATORS','ETHERNET','STORAGE','SERVICE','COOLING','DEBUG']
for n in ['PiSXMe_RevA_Clean.kicad_sch','PiSXMe_RevA_Clean.kicad_pro','PiSXMe_RevA_Clean_complete.kicad_sym','Storage_DualMode.kicad_sym','sym-lib-table','fp-lib-table']+[x+'.kicad_sch' for x in children]:shutil.copy2(R/n,OUT/n)
shutil.copytree(R/'PiSXMe_RevA_Clean.pretty',OUT/'PiSXMe_RevA_Clean.pretty')
names={'NC_62','NC_61','NC_59','NC_58','NC_57','NC_52','NC_20','NC_19','NC_15','NC_14','NC_13','NC_9','NC_8','NC_7','NC_6','NC_5','NC_4','NC_3','NC_2','NC_1'}
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
     if depth==0:
      yield i,j+1,s[i:j+1];i=j+1;break
   j+=1
  else:return
p=OUT/'STORAGE.kicad_sch';s=p.read_text();found=[]
for start,end,rec in records(s):
 name=rec.split('"',2)[1]
 if name in names and '(at 70 ' in rec:found.append((start,end,name))
for start,end,name in reversed(found):s=s[:start]+s[end:]
p.write_text(s);print('removed_records',len(found))
r=subprocess.run(['flatpak','run','--command=kicad-cli','org.kicad.KiCad','sch','erc','--severity-all','--output',str(OUT/'erc.rpt'),str(OUT/'PiSXMe_RevA_Clean.kicad_sch')],cwd=OUT,text=True,capture_output=True);print(r.stdout.strip());print(r.stderr.strip());print('erc_rc',r.returncode)
