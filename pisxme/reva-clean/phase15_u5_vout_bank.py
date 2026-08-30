"""Place and fan out U5's 1.1 V output capacitor bank."""
from pathlib import Path
import pcbnew

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'ACREAGE_U4_U5_CONTROLS_PHASE15.kicad_pcb'
OUTPUT=ROOT/'ACREAGE_U5_VOUT_PHASE15.kicad_pcb'
def mm(x,y): return pcbnew.VECTOR2I_MM(x,y)
def pad(b,r,n): return next(p for p in b.FindFootprintByReference(r).Pads() if str(p.GetNumber())==str(n))
def tr(b,a,z,n,w=.50,layer=pcbnew.F_Cu):
    t=pcbnew.PCB_TRACK(b); t.SetStart(a); t.SetEnd(z); t.SetLayer(layer); t.SetWidth(pcbnew.FromMM(w)); t.SetNet(n); b.Add(t)
def via(b,xy,n):
    q=pcbnew.PCB_VIA(b); q.SetPosition(xy); q.SetWidth(pcbnew.FromMM(.50)); q.SetDrill(pcbnew.FromMM(.30)); q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNet(n); b.Add(q)
def put(b,r,x,y):
    f=b.FindFootprintByReference(r); f.SetPosition(mm(x,y)); f.SetOrientationDegrees(0)
def main():
    b=pcbnew.LoadBoard(str(INPUT))
    refs=[f'C{i}' for i in range(26,42)]
    for i,r in enumerate(refs):
        # Keep all four rows beside U5; the PG support island is offset left.
        row = i // 4
        x0 = 240
        put(b,r,x0+(i%4)*8,115+row*8)
    out=pad(b,'U5','8').GetNet()
    # Leave the U5 left output land by the package edge, then use a broad
    # local trunk feeding each capacitor row.  Every endpoint is taken from
    # the loaded pad geometry rather than a hard-coded pad center.
    # Use the right output land.  The left side is the compact VIN/EN escape
    # field; leaving from pad 9 avoids crossing that authoritative 12 V path.
    u5=pad(b,'U5','9'); edge=pcbnew.VECTOR2I(u5.GetPosition().x+int(u5.GetSize().x/2),u5.GetPosition().y)
    trunk_x=238; root_x=234; trunk_top=mm(trunk_x,109); trunk_bottom=mm(trunk_x,141)
    # Drop immediately at the right edge, below the FB vertical escape, then
    # move right.  Moving laterally at y=107 would cross that FB escape.
    drop=mm(228.15,111)
    root_at_edge=mm(root_x,111)
    root=mm(root_x,109)
    tr(b,edge,drop,out,.30)
    tr(b,drop,root_at_edge,out,.30)
    tr(b,root_at_edge,root,out,.30)
    tr(b,root,trunk_top,out,.60,pcbnew.In2_Cu)
    via(b,root,out); via(b,trunk_top,out); tr(b,trunk_top,trunk_bottom,out, .60, pcbnew.In2_Cu)
    for row in range(4):
        row_y=115+row*8
        row_pad=[pad(b,r,'1') for r in refs[row*4:(row+1)*4]]
        for p in row_pad:
            anchor=pcbnew.VECTOR2I(p.GetPosition().x,pcbnew.FromMM(row_y+2))
            via(b,anchor,out)
            tr(b,p.GetPosition(),anchor,out)
            tr(b,pcbnew.VECTOR2I(pcbnew.FromMM(trunk_x),anchor.y),anchor,out,.60,pcbnew.In2_Cu)
            # Keep each output-capacitor return local.  The via sits just
            # outside the authoritative ground land, avoiding a solder-mask
            # bridge, and a short top-layer link reaches the pad.
            gp = pad(b,r,'2')
            gvia = pcbnew.VECTOR2I(gp.GetPosition().x + pcbnew.FromMM(1.8), gp.GetPosition().y)
            via(b,gvia,gp.GetNet())
            gedge = pcbnew.VECTOR2I(gp.GetPosition().x + int(gp.GetSize().x / 2), gp.GetPosition().y)
            tr(b,gedge,gvia,gp.GetNet(),.30)
    pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUTPUT))
    print('Phase 15 U5 VOUT bank: candidate generated; 16 capacitors on In2.Cu trunk')
if __name__=='__main__': main()
