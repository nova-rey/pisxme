"""Local SATA TX_P length-match probe on the split-cap V3 island."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE19_V3_USB_PROVEN_SPLIT_SATA_REFILL.kicad_pcb'
OUT=R/'PHASE19_V3_USB_PROVEN_SPLIT_SATA_TX_MATCH.kicad_pcb'
V=lambda x,y: pcbnew.VECTOR2I_MM(x,y)
def main():
 b=pcbnew.LoadBoard(str(BASE)); n=b.FindNet('/STORAGE/BRIDGE_SATA_TX_P')
 # Resolve the live width and net before mutating the track collection.
 old=[]; rxold=[]; width=pcbnew.FromMM(.13208); rxwidth=width
 for t in b.GetTracks():
  if t.Type()!=14 and (t.GetNetname()=='/STORAGE/BRIDGE_SATA_TX_P' or t.GetNetname()=='/STORAGE/BRIDGE_SATA_RX_P'):
   a=(round(pcbnew.ToMM(t.GetStart().x),3),round(pcbnew.ToMM(t.GetStart().y),3));z=(round(pcbnew.ToMM(t.GetEnd().x),3),round(pcbnew.ToMM(t.GetEnd().y),3))
   if {a,z}=={(120.5,133.0),(126.0,130.0)} and t.GetLayer()==pcbnew.B_Cu:
    old.append(t); width=t.GetWidth()
   if {a,z}=={(119.0,120.0),(126.0,120.0)} and t.GetLayer()==pcbnew.B_Cu:
    rxold.append(t); rxwidth=t.GetWidth()
 for t in old:b.Remove(t)
 for t in rxold:b.Remove(t)
 # Keep the existing source via and cap endpoints.  The detour stays outside
 # the U7 body and J3/cap field, adding roughly 30 mm to TX_P on B.Cu.
 pts=[(120.5,133.0),(126.0,133.0),(126.0,150.0),(135.5,150.0),(135.5,130.0),(126.0,130.0)]
 for a,z in zip(pts,pts[1:]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(V(*a));q.SetEnd(V(*z));q.SetLayer(pcbnew.B_Cu);q.SetWidth(width);q.SetNet(n);b.Add(q)
 rn=b.FindNet('/STORAGE/BRIDGE_SATA_RX_P')
 for a,z in zip([(119.0,120.0),(119.0,122.0),(130.0,122.0),(130.0,120.0)],[(119.0,122.0),(130.0,122.0),(130.0,120.0),(126.0,120.0)]):
  q=pcbnew.PCB_TRACK(b);q.SetStart(V(*a));q.SetEnd(V(*z));q.SetLayer(pcbnew.B_Cu);q.SetWidth(rxwidth);q.SetNet(rn);b.Add(q)
 b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
