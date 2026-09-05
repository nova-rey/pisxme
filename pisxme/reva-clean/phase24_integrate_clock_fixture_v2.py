"""Transform the passing V2 clock fixture into the current U7 acreage frame."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE24_U7_CLOCK_NET_AUTHORITY.kicad_pcb"
FIXTURE = R / "PHASE24_COMPLETE_CLOCK_FIXTURE_V2.kicad_pcb"
OUT = R / "PHASE24_CLOCK_FIXTURE_V2_TRANSFORMED.kicad_pcb"
CLOCK = {"/STORAGE/BRIDGE_XI", "/STORAGE/BRIDGE_XO", "/STORAGE/BRIDGE_VSSOSC"}

def V(x, y): return pcbnew.VECTOR2I_MM(x, y)
def transform(p): return V(220 - pcbnew.ToMM(p.x), 240 - pcbnew.ToMM(p.y))

def main():
    board = pcbnew.LoadBoard(str(BASE)); fixture = pcbnew.LoadBoard(str(FIXTURE))
    nets = {name: board.FindNet(name) for name in CLOCK}
    for item in list(board.GetTracks()):
        if item.GetNetname() in CLOCK:
            board.RemoveNative(item)
    fmap = {"Y1": "Y1", "R23": "R23", "C42": "C42", "C43": "C43"}
    for ref in fmap:
        board.FindFootprintByReference(ref).SetPosition(transform(fixture.FindFootprintByReference(ref).GetPosition()))
        board.FindFootprintByReference(ref).SetOrientationDegrees(180)
    for item in fixture.GetTracks():
        if item.GetNetname() not in CLOCK:
            continue
        net = nets[item.GetNetname()]
        if type(item).__name__ == "PCB_VIA":
            via = pcbnew.PCB_VIA(board); via.SetPosition(transform(item.GetPosition()))
            via.SetWidth(item.GetWidth(pcbnew.F_Cu)); via.SetDrill(item.GetDrill())
            via.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu); via.SetNet(net); board.Add(via)
        else:
            track = pcbnew.PCB_TRACK(board); track.SetStart(transform(item.GetStart()))
            track.SetEnd(transform(item.GetEnd())); track.SetLayer(item.GetLayer())
            track.SetWidth(item.GetWidth()); track.SetNet(net); board.Add(track)
    board.Save(str(OUT)); print(OUT)

if __name__ == "__main__": main()
