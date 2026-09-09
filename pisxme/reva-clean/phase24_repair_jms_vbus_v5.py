"""Disposable native-pad VBUS/sense escape against the J8 V5 basis."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; b=pcbnew.LoadBoard(str(R/'PHASE24_STORAGE_NETLIST_REGENERATED_J8_V5.kicad_pcb')); F,B=pcbnew.F_Cu,pcbnew.B_Cu
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def pad(r,n): return b.FindFootprintByReference(r).FindPadByNumber(str(n))
def xy(q): return pcbnew.ToMM(q.GetPosition().x),pcbnew.ToMM(q.GetPosition().y)
def tr(n,a,z,l):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.2));t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(*q));v.SetWidth(pcbnew.FromMM(.55));v.SetDrill(pcbnew.FromMM(.3));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
for name,src_ref,src_pin,dst_ref,dst_pin,sv,ev in [
 ('VBUS','U11','16','R82','1',(137.0,138.0),(129.0,115.0)),
 ('JMS_VBUS_SENSE','U11','10','R83','1',(135.0,135.6),(135.0,115.0))]:
 n=b.FindNet(name)
 for t in list(b.GetTracks()):
  if t.GetNetCode()==n.GetNetCode(): b.RemoveNative(t)
 s=xy(pad(src_ref,src_pin)); d=xy(pad(dst_ref,dst_pin)); via(n,sv); via(n,ev)
 tr(n,s,sv,F); tr(n,sv,ev,B); tr(n,ev,d,F)
# Divider midpoint is a separate source-owned segment between the two
# resistor pads; it is intentionally not inferred from same-net proximity.
sn=b.FindNet('JMS_VBUS_SENSE'); tr(sn,xy(pad('R82','2')),xy(pad('R83','1')),F)
b.BuildListOfNets();out=R/'PHASE24_STORAGE_J8_V5_VBUS_V1.kicad_pcb';b.Save(str(out));print(out)
