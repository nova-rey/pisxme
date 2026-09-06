"""Route the low-speed JMS583 support network in a disposable PCB candidate.

This intentionally leaves high-speed USB/PCIe/SATA channels for their own
constraint-aware router. Every endpoint is resolved from native pad objects.
"""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'PHASE24_DUAL_MODE_STORAGE_PLACEMENT.kicad_pcb'
OUT=R/'PHASE24_DUAL_MODE_STORAGE_SUPPORT_ROUTED.kicad_pcb'
def V(p): return pcbnew.VECTOR2I_MM(float(p[0]),float(p[1]))
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def net(b,name):
 n=b.FindNet(name)
 if n is None: raise RuntimeError('missing native net '+name)
 return n
def pad(b,ref,num):
 f=b.FindFootprintByReference(ref)
 if f is None: raise RuntimeError('missing '+ref)
 p=f.FindPadByNumber(str(num))
 if p is None: raise RuntimeError(f'missing {ref}.{num}')
 return p
def track(b,n,a,z,layer=pcbnew.F_Cu,w=.18):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(a)); t.SetEnd(V(z)); t.SetLayer(layer); t.SetWidth(pcbnew.FromMM(w)); t.SetNet(n); b.Add(t)
def join(b,na,ra,pa,rb,pb):
 a=xy(pad(b,ra,pa).GetPosition()); z=xy(pad(b,rb,pb).GetPosition())
 track(b,net(b,na),a,z)
def main():
 b=pcbnew.LoadBoard(str(BASE))
 # Direct support relationships from JMS583 Rev 2.1. These are native-pad
 # endpoints, not synthetic graph edges.
 jobs=[
  ('JMS_REXT','U11','39','R80','1'),
  ('POWER_GND','R80','2','U11','63'),
  ('JMS_LXO','U11','64','L10','1'),
  ('JMS_VDDREG_5V','L10','2','U11','1'),
  ('JMS_XIN','U11','50','Y10','1'),('JMS_XOUT','U11','51','Y10','2'),
  ('POWER_GND','Y10','3','Y10','4'),
  ('JMS_AVDD33','U11','19','C80','1'),('POWER_GND','U11','63','C80','2'),
  ('JMS_RESET_N','U11','15','R81','1'),
  ('POWER_GND','U11','63','C85','2'),
  ('VBUS','U11','16','R82','1'),('JMS_VBUS_SENSE','R82','2','R83','1'),
  ('POWER_GND','R83','2','U11','63'),
 ]
 for n,ra,pa,rb,pb in jobs: join(b,n,ra,pa,rb,pb)
 b.Save(str(OUT)); print(OUT, len(jobs))
if __name__=='__main__': main()
