"""Single-net SPICS layer-transition discriminator after U2 co-location."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_SUPPORT_RELOCATION_U2_V1.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_SPICS_LAYER_PROBE_V1.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu;W=pcbnew.FromMM(.20)
def P(x,y):return pcbnew.VECTOR2I_MM(float(x),float(y))
def seg(b,n,l,a,z):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(W);t.SetNet(n);t.SetNetCode(n.GetNetCode());b.Add(t)
def via(b,n,q):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*q));v.SetWidth(pcbnew.FromMM(.60));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(F,B);v.SetNet(n);v.SetNetCode(n.GetNetCode());b.Add(v)
def main():
 b=pcbnew.LoadBoard(str(BASE));n=b.FindNet('SPICS')
 seg(b,n,F,(101.95,70.8),(103.0,70.8));seg(b,n,F,(103.0,70.8),(103.0,69.0));via(b,n,(103.0,69.0))
 seg(b,n,B,(103.0,69.0),(103.0,60.0));seg(b,n,B,(103.0,60.0),(106.0,60.0))
 seg(b,n,B,(106.0,60.0),(106.0,75.0));seg(b,n,B,(106.0,75.0),(110.8,75.0))
 via(b,n,(110.8,75.0));seg(b,n,F,(110.8,75.0),(110.8,76.0))
 b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
