"""Minimal U7 rotation-270 clock/SATA pad-field escape fixture."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE19_COORDINATED_U7ROT270_FULL.kicad_pcb'; OUT=R/'PHASE19_U7ROT270_PADFIELD_FIXTURE.kicad_pcb'
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def T(b,n,a,z,l=pcbnew.F_Cu):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(l); t.SetWidth(pcbnew.FromMM(.2)); t.SetNet(n); b.Add(t)
def X(b,n,p):
 v=pcbnew.PCB_VIA(b); v.SetPosition(V(*p)); v.SetWidth(pcbnew.FromMM(.5)); v.SetDrill(pcbnew.FromMM(.3)); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(n); b.Add(v)
def main():
 b=pcbnew.LoadBoard(str(BASE)); u=b.FindFootprintByReference('U7')
 footprints=list(b.GetFootprints()); tracks=list(b.GetTracks()); zones=list(b.Zones())
 for f in footprints:
  if f.GetReference()!='U7': b.Remove(f)
 for t in tracks: b.Remove(t)
 for z in zones: b.Remove(z)
 names=['/STORAGE/BRIDGE_XI','/STORAGE/BRIDGE_XO','/STORAGE/BRIDGE_VSSOSC','/STORAGE/BRIDGE_3V3','/STORAGE/BRIDGE_SATA_TX_P','/STORAGE/BRIDGE_SATA_TX_N','/STORAGE/BRIDGE_SATA_RX_P','/STORAGE/BRIDGE_SATA_RX_N']
 nets={n:b.FindNet(n) for n in names}
 for n in names:
  if nets[n] is None:
   nets[n]=pcbnew.NETINFO_ITEM(b,n); nets[n].SetNetCode(b.GetNetCount()+1); b.Add(nets[n])
 pinmap={'52':names[0],'53':names[2],'54':names[1],'57':names[4],'56':names[5],'60':names[6],'59':names[7]}
 for pin,n in pinmap.items():
  p=next(p for p in u.Pads() if str(p.GetNumber())==pin); p.SetNet(nets[n]); p.SetNetCode(nets[n].GetNetCode())
 # Rot270 coordinates: clock x=135.5,y=127..128; SATA x=135.5,y=129..131.
 # Clock escapes west, SATA escapes east, with all crossings outside the row.
 T(b,nets[names[0]],(135.5,127),(130,127)); T(b,nets[names[2]],(135.5,127.5),(130,127.5)); T(b,nets[names[1]],(135.5,128),(130,128))
 T(b,nets[names[4]],(135.5,129.5),(141,129.5)); T(b,nets[names[5]],(135.5,129),(141,129),pcbnew.B_Cu)
 T(b,nets[names[6]],(135.5,131),(141,131)); T(b,nets[names[7]],(135.5,130.5),(141,130.5),pcbnew.B_Cu)
 b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
