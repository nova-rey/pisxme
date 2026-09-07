"""V227: co-author SPISO3 and PERST in the U1 right-side source field."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent
BASE=HERE/'PHASE24_RTL9210B_PEDET_R2_U18_J1_69_V215.kicad_pcb'
OUT=HERE/'PHASE24_RTL9210B_QFN_SIDEBAND_SPISO3_PERST_V227.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu
def p(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def add(b,code,l,a,z):
    t=pcbnew.PCB_TRACK(b);t.SetStart(p(*a));t.SetEnd(p(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(.20));t.SetNetCode(code);b.Add(t)
def via(b,code,x,y):
    v=pcbnew.PCB_VIA(b);v.SetPosition(p(x,y));v.SetNetCode(code);b.Add(v)
def remove_net(b,name):
    net=b.FindNet(name)
    if not hasattr(net,'GetNetCode'): return
    code=net.GetNetCode()
    for item in list(b.GetTracks()):
        if item.GetNetCode()==code: b.Remove(item)
def main():
    b=pcbnew.LoadBoard(str(BASE))
    spiso3_code=b.FindNet('SPISO3').GetNetCode()
    perst_code=b.FindNet('PERST_N').GetNetCode()
    for item in list(b.GetTracks()):
        if item.GetNetCode() in {spiso3_code, perst_code}: b.Remove(item)
    s=spiso3_code
    add(b,s,F,(99.6,58.05),(99.8,56.8));via(b,s,99.8,56.8)
    add(b,s,B,(99.8,56.8),(106.5,56.8));via(b,s,106.5,56.8)
    add(b,s,F,(106.5,56.8),(106.5,74.0));add(b,s,F,(106.5,74.0),(89.0,74.0));add(b,s,F,(89.0,74.0),(89.0,72.0))
    r=perst_code
    add(b,r,F,(101.95,60.0),(104.5,60.0));add(b,r,F,(104.5,60.0),(104.5,63.0));via(b,r,104.5,63.0)
    add(b,r,B,(104.5,63.0),(104.5,72.0));add(b,r,B,(104.5,72.0),(134.5,72.0));via(b,r,134.5,72.0)
    add(b,r,F,(134.5,72.0),(136.0,70.28))
    b.BuildListOfNets();b.Save(str(OUT));print(OUT)
if __name__=='__main__': main()
