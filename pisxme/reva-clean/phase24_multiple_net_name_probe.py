"""Disposable probe for co-located STORAGE alias labels."""
from pathlib import Path
import re, shutil, subprocess

HERE = Path(__file__).resolve().parent
OUT = HERE / ".phase24_multiple_net_name_probe"
CHILDREN = ("CORE_CM5","V100_PCIE","V100_POWER","POWER_INPUT","REGULATORS","ETHERNET","STORAGE","SERVICE","COOLING","DEBUG")

def expr_end(s, start):
    d=0; q=False; esc=False
    for i in range(start,len(s)):
        c=s[i]
        if q and esc: esc=False
        elif q and c=='\\': esc=True
        elif c=='"': q=not q
        elif not q and c=='(': d+=1
        elif not q and c==')':
            d-=1
            if d==0: return i+1
    raise ValueError(start)

def labels(s):
    out=[]; pos=0
    while True:
        m=re.search(r'\n\s*\(label "([^"]+)"',s[pos:])
        if not m: return out
        st=pos+m.start()+1
        en=expr_end(s,st)
        b=s[st:en]; at=re.search(r'\(at ([0-9.+-]+) ([0-9.+-]+)',b)
        out.append((st,en,m.group(1),tuple(at.groups()) if at else None))
        pos=en

if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir()
for name in ["PiSXMe_RevA_Clean.kicad_sch", "PiSXMe_RevA_Clean.kicad_pro", *[x+".kicad_sch" for x in CHILDREN], "PiSXMe_RevA_Clean_complete.kicad_sym", "sym-lib-table", "Storage_DualMode.kicad_sym"]:
    shutil.copy2(HERE/name, OUT/name)
p=OUT/"STORAGE.kicad_sch"; s=p.read_text()
ls=labels(s); by={}
for x in ls:
    if x[3]: by.setdefault(x[3],[]).append(x)
remove=[]
for at, group in by.items():
    if any(not n.startswith('NC_') for _,_,n,_ in group):
        remove.extend((a,b) for a,b,n,_ in group if n.startswith('NC_'))
for a,b in reversed(remove): s=s[:a]+s[b:]
p.write_text(s)
print(f"removed={len(remove)} output={OUT}")
report=OUT/"no-nc-alias-erc.rpt"
cmd=["flatpak","run","--command=kicad-cli","org.kicad.KiCad","sch","erc","--severity-all","--output",str(report),str(OUT/"PiSXMe_RevA_Clean.kicad_sch")]
r=subprocess.run(cmd,cwd=OUT,text=True,capture_output=True)
print(r.stdout.strip()); print(r.stderr.strip()); print(f"erc_rc={r.returncode} report={report}")
