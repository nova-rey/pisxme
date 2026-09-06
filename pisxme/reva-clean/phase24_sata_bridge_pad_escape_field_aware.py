"""Disposable field-aware U7 SATA escape; vias leave the pad row vertically."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent; BASE=R/'PHASE24_STORAGE_ISLAND_COHERENT_USB3_REPAIRED.kicad_pcb'; OUT=R/'PHASE24_STORAGE_ISLAND_COHERENT_USB3_SATA_BRIDGE_ESCAPE_FIELD_AWARE.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.13208)
def V(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def xy(p): q=p.GetPosition() if hasattr(p,'GetPosition') else p; return pcbnew.ToMM(q.x),pcbnew.ToMM(q.y)
def pad(b,r,n): return b.FindFootprintByReference(r).FindPadByNumber(str(n))
def tr(b,n,a,z,l):
 t=pcbnew.PCB_TRACK(b);t.SetStart(V(*a));t.SetEnd(V(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);b.Add(t)
def via(b,n,p):
 v=pcbnew.PCB_VIA(b);v.SetPosition(V(*p));v.SetWidth(pcbnew.FromMM(.50));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);b.Add(v)
b=pcbnew.LoadBoard(str(BASE)); jobs=(('TX_P','57','C30','2'),('TX_N','56','C31','2'),('RX_P','60','C32','2'),('RX_N','59','C33','2'))
for t in list(b.GetTracks()):
 if t.GetNetname() in {'/STORAGE/BRIDGE_SATA_'+x[0] for x in jobs}: b.Remove(t)
plans={
 'TX_P':((110.5,99.5),(116.0,99.5),(116.0,96.5),(117.5,97.0)),
 'TX_N':((111.0,99.0),(115.5,99.0),(115.5,113.0),(117.5,113.0)),
 'RX_P':((109.0,98.0),(123.0,98.0),(123.0,96.5),(123.5,97.0)),
 'RX_N':((109.5,98.5),(175.0,98.5),(175.0,115.0),(123.5,115.0)),
}
for key,jp,cap,cp in jobs:
 n=b.FindNet('/STORAGE/BRIDGE_SATA_'+key); src=xy(pad(b,'U7',jp)); dst=xy(pad(b,cap,cp)); a,bp,cpnt,end=plans[key]
 tr(b,n,src,a,F); via(b,n,a); tr(b,n,a,bp,B); via(b,n,bp)
 if key=='RX_N':
  tr(b,n,bp,cpnt,B); via(b,n,cpnt)
 else: tr(b,n,bp,cpnt,F)
 tr(b,n,cpnt,end,F); tr(b,n,end,dst,F)
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
