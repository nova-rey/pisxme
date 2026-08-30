"""Vendor-style FB/RT/PG corridors for the separated U4/U5 islands."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "ACREAGE_U3_CONTROLS_PHASE15.kicad_pcb"
OUTPUT = ROOT / "ACREAGE_U4_U5_CONTROLS_PHASE15.kicad_pcb"

def v(x, y): return pcbnew.VECTOR2I_MM(x, y)
def getpad(board, ref, number):
    return next(p for p in board.FindFootprintByReference(ref).Pads()
                if str(p.GetNumber()) == str(number))
def net(board, name):
    return next(n for k, n in board.GetNetsByName().items() if str(k) == name)
def tr(board, a, b, n, layer=pcbnew.F_Cu, width=.20):
    t=pcbnew.PCB_TRACK(board); t.SetStart(a); t.SetEnd(b); t.SetLayer(layer)
    t.SetWidth(pcbnew.FromMM(width)); t.SetNet(n); board.Add(t)
def via(board, xy, n):
    q=pcbnew.PCB_VIA(board); q.SetPosition(xy); q.SetWidth(pcbnew.FromMM(.50))
    q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu)
    q.SetNet(n); board.Add(q)
def put(board, ref, x, y, angle=0):
    f=board.FindFootprintByReference(ref); f.SetPosition(v(x,y)); f.SetOrientationDegrees(angle)

def island(board, reg, pin, root_xy, corridor_y, supports):
    rp=getpad(board,reg,pin); n=rp.GetNet()
    edge=pcbnew.VECTOR2I(rp.GetPosition().x + int(rp.GetSize().x/2), rp.GetPosition().y)
    root=v(*root_xy)
    # A short F.Cu edge escape followed by a B.Cu vertical transition keeps
    # the control route out of the adjacent high-current pin field.
    neck=pcbnew.VECTOR2I(pcbnew.FromMM(root_xy[0]), rp.GetPosition().y)
    tr(board, edge, neck, n)
    # A jogged root is used where adjacent 0.5 mm-pitch pins would otherwise
    # put a through-via beside the neighboring pin escape.
    if root.y != neck.y:
        tr(board, neck, pcbnew.VECTOR2I(neck.x, root.y), n)
    tr(board, pcbnew.VECTOR2I(neck.x, root.y), root, n)
    via(board, root, n)
    trunk=v(root_xy[0], corridor_y)
    tr(board, root, trunk, n, pcbnew.B_Cu)
    for ref,num in supports:
        p=getpad(board,ref,num)
        if p.GetNetname() != n.GetNetname(): raise SystemExit(f"{ref}.{num} net mismatch")
        anchor=pcbnew.VECTOR2I(p.GetPosition().x, pcbnew.FromMM(corridor_y))
        via(board, anchor, n)
        tr(board,p.GetPosition(),anchor,n)
        tr(board,anchor,trunk,n,pcbnew.B_Cu)

def main():
    b=pcbnew.LoadBoard(str(INPUT))
    # U4 at (200,105), controls above the module.
    for ref,xy,ang in (("C18",(180,70),0),("R11",(188,70),0),
                       ("R12",(196,70),0),("R13",(212,82),0),
                       ("R14",(218,76),0)):
        put(b,ref,*xy,ang)
    island(b,"U4","10",(204,106.25),66,(("C18","1"),("R11","2"),("R12","1")))
    island(b,"U4","13",(206,101.0),72,(("R14","2"),))
    island(b,"U4","12",(212,103.0),78,(("R13","1"),))
    # U5 at (225,105), controls below the module and clear of U7.
    for ref,xy,ang in (("R19",(245,150),0),("R20",(253,150),0),
                       ("R21",(234,145),0),("R22",(236,145),0)):
        put(b,ref,*xy,ang)
    island(b,"U5","10",(229,110.0),150,(("R19","2"),("R20","1")))
    island(b,"U5","13",(230,101.0),145,(("R22","2"),))
    island(b,"U5","12",(232,103.0),140,(("R21","1"),))
    # C18 is the U4 feed-forward capacitor; its output side must land on the
    # same local VOUT copper as the C16/C17/C19 output bank.
    c18=getpad(b,"C18","2"); c16=getpad(b,"C16","1"); out=c16.GetNet()
    c18_route=pcbnew.VECTOR2I(c18.GetPosition().x,pcbnew.FromMM(64))
    # Approach the output pad from the right; the input capacitor bank sits
    # directly above the C16 left-side return and must not be crossed.
    c16_route=pcbnew.VECTOR2I(pcbnew.FromMM(216),pcbnew.FromMM(64))
    c16_drop=pcbnew.VECTOR2I(pcbnew.FromMM(216),c16.GetPosition().y)
    tr(b,c18.GetPosition(),c18_route,out)
    tr(b,c18_route,c16_route,out)
    tr(b,c16_route,c16_drop,out)
    tr(b,c16_drop,c16.GetPosition(),out)
    pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUTPUT))
    print("Phase 15 U4/U5 controls: candidate generated with separated B.Cu trunks")
if __name__ == "__main__": main()
