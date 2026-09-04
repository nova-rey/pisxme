"""Try an acreage top-edge SATA corridor, clear of the frozen PCIe trunk."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / 'ACREAGE_PHASE18_USB3_LOCAL.kicad_pcb'
OUT = ROOT / 'ACREAGE_PHASE19_SATA_TOP_EDGE.kicad_pcb'
W = pcbnew.FromMM(.15)

def V(x, y): return pcbnew.VECTOR2I_MM(x, y)
def xy(p): return (pcbnew.ToMM(p.GetPosition().x), pcbnew.ToMM(p.GetPosition().y))
def pad(fp, number): return next(p for p in fp.Pads() if str(p.GetNumber()) == str(number))
def track(b, net, a, z, layer):
    t = pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer)
    t.SetWidth(W); t.SetNet(net); b.Add(t)
def via(b, net, x, y):
    q = pcbnew.PCB_VIA(b); q.SetPosition(V(x, y)); q.SetWidth(pcbnew.FromMM(.5))
    q.SetDrill(pcbnew.FromMM(.3)); q.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
    q.SetNet(net); b.Add(q)

def main():
    b = pcbnew.LoadBoard(str(BASE))
    u, j = b.FindFootprintByReference('U7'), b.FindFootprintByReference('J3')
    u.SetPosition(V(110, 105)); u.SetOrientationDegrees(180)
    j.SetPosition(V(200, 60)); j.SetOrientationDegrees(0)
    # Go above the existing PCIe branch and CM5_PERST vertical, then split
    # RX to B.Cu and TX to F.Cu so the two pairs never share a corridor.
    specs = (
        ('BRIDGE_SATA_RX_P', '60', '3', (109, 84), (165, 78), pcbnew.B_Cu),
        ('BRIDGE_SATA_RX_N', '59', '4', (109.5, 83), (166, 77), pcbnew.B_Cu),
        ('BRIDGE_SATA_TX_P', '57', '1', (110.5, 86), (180, 86), pcbnew.F_Cu),
        ('BRIDGE_SATA_TX_N', '56', '2', (111, 87), (181, 87), pcbnew.F_Cu),
    )
    for name, up, jp, first, turn, layer in specs:
        net = b.FindNet('/STORAGE/' + name)
        a, z = pad(u, up), pad(j, jp); a.SetNet(net); z.SetNet(net)
        track(b, net, xy(a), first, pcbnew.F_Cu); via(b, net, *first)
        track(b, net, first, turn, layer); track(b, net, turn, xy(z), layer)
    b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)

if __name__ == '__main__': main()
