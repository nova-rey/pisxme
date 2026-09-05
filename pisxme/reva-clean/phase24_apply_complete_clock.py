"""Compose the native-clean complete clock copper onto the Phase 24 ancestor."""
from pathlib import Path
import pcbnew
R=Path(__file__).resolve().parent
BASE=R/'PHASE24_LOCAL_REPAIRS_U7_RXN.kicad_pcb'
SOURCE=R/'PHASE24_CLOCK_COMPLETE_ASTAR_V2.kicad_pcb'
OUT=R/'PHASE24_LOCAL_REPAIRS_CLOCK_COMPLETE.kicad_pcb'
CLOCK={'/STORAGE/BRIDGE_XI','/STORAGE/BRIDGE_XO','/STORAGE/BRIDGE_VSSOSC'}
def copy_item(board,item,net):
    if type(item).__name__=='PCB_VIA':
        v=pcbnew.PCB_VIA(board); v.SetPosition(item.GetPosition()); v.SetWidth(item.GetWidth(pcbnew.F_Cu)); v.SetDrill(item.GetDrill()); v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); v.SetNet(net); board.Add(v)
    else:
        t=pcbnew.PCB_TRACK(board); t.SetStart(item.GetStart()); t.SetEnd(item.GetEnd()); t.SetLayer(item.GetLayer()); t.SetWidth(item.GetWidth()); t.SetNet(net); board.Add(t)
def main():
    b=pcbnew.LoadBoard(str(BASE)); s=pcbnew.LoadBoard(str(SOURCE)); nets={n:b.FindNet(n) for n in CLOCK}
    for item in list(b.GetTracks()):
        if item.GetNetname() in CLOCK: b.RemoveNative(item)
    for item in s.GetTracks():
        if item.GetNetname() in CLOCK: copy_item(b,item,nets[item.GetNetname()])
    # Preserve source pad net/layer authority for support passives and U7.
    for ref in ('U7','Y1','R23','C42','C43'):
        dst=b.FindFootprintByReference(ref); src=s.FindFootprintByReference(ref)
        for dp,sp in zip(dst.Pads(),src.Pads()):
            if sp.GetNetname() in CLOCK:
                dp.SetNet(nets[sp.GetNetname()]); dp.SetNetCode(nets[sp.GetNetname()].GetNetCode()); dp.SetLayerSet(sp.GetLayerSet())
    b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
