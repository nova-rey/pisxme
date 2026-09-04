"""Route SATA around the right endpoint of the frozen PCIe B.Cu trunk."""
from pathlib import Path
import pcbnew

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'ACREAGE_PHASE18_USB3_LOCAL.kicad_pcb'
OUT=ROOT/'ACREAGE_PHASE19_SATA_ENDPOINT.kicad_pcb'
W=pcbnew.FromMM(0.15)

def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def add(board,net,a,b,layer):
    t=pcbnew.PCB_TRACK(board); t.SetStart(V(*a)); t.SetEnd(V(*b)); t.SetLayer(layer); t.SetWidth(W); t.SetNet(net); board.Add(t)
def addvia(board,net,x,y):
    q=pcbnew.PCB_VIA(board); q.SetPosition(V(x,y)); q.SetWidth(pcbnew.FromMM(.5)); q.SetDrill(pcbnew.FromMM(.3)); q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNet(net); board.Add(q)
def p(fp,n): return next(x for x in fp.Pads() if str(x.GetNumber())==str(n))
def xy(q): return (pcbnew.ToMM(q.GetPosition().x),pcbnew.ToMM(q.GetPosition().y))

def main():
    b=pcbnew.LoadBoard(str(BASE)); u=b.FindFootprintByReference('U7'); j=b.FindFootprintByReference('J3')
    if not u or not j: raise RuntimeError('U7/J3 missing')
    u.SetPosition(V(110,105)); u.SetOrientationDegrees(180)
    j.SetPosition(V(190,130)); j.SetOrientationDegrees(90)
    specs=(
      # One pair per layer.  Turn columns are reverse-ordered within each
      # layer so the vertical drops cannot intersect the companion lane.
      ('BRIDGE_SATA_RX_P','60','3',(108,98),(173,98),(173,138.75),pcbnew.B_Cu),
      ('BRIDGE_SATA_RX_N','59','4',(109.5,99),(171,99),(171,138.5),pcbnew.B_Cu),
      ('BRIDGE_SATA_TX_P','57','1',(111,96),(177,96),(177,139.25),pcbnew.F_Cu),
      ('BRIDGE_SATA_TX_N','56','2',(112.5,97),(175,97),(175,139.0),pcbnew.F_Cu),
    )
    for name,up,jp,first,turn,down,layer in specs:
        net=b.FindNet('/STORAGE/'+name)
        if not net: raise RuntimeError('missing net '+name)
        a=p(u,up); z=p(j,jp); a.SetNet(net); z.SetNet(net)
        add(b,net,xy(a),first,pcbnew.F_Cu); addvia(b,net,*first)
        add(b,net,first,turn,layer); add(b,net,turn,down,layer)
        add(b,net,down,xy(z),layer)
    b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
