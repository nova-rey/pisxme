"""V1300: transplant the native V1195 crystal/RSET routes into V1279."""
from pathlib import Path
import pcbnew
H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_XTAL_IN_LIVE_PAD_V1279.kicad_pcb'
DONOR=H/'PHASE24_RTL9210B_QFN_XTAL_3V3_COAUTHOR_V1195.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_V1279_V1195_CLOCK_RSET_TRANSPLANT_V1300.kicad_pcb'
NETS={'RSET','XTAL_IN','XTAL_OUT'}
def clone(board, item, net):
    if type(item).__name__ == 'PCB_VIA':
        x=pcbnew.PCB_VIA(board); x.SetPosition(item.GetPosition()); x.SetWidth(item.GetWidth()); x.SetDrill(item.GetDrill()); x.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
    else:
        x=pcbnew.PCB_TRACK(board); x.SetStart(item.GetStart()); x.SetEnd(item.GetEnd()); x.SetLayer(item.GetLayer()); x.SetWidth(item.GetWidth())
    x.SetNet(net); x.SetNetCode(net.GetNetCode()); board.Add(x)
b=pcbnew.LoadBoard(str(BASE)); d=pcbnew.LoadBoard(str(DONOR))
for item in list(b.GetTracks()):
    if item.GetNetname() in NETS: b.RemoveNative(item)
for item in d.GetTracks():
    if item.GetNetname() in NETS: clone(b,item,b.FindNet(item.GetNetname()))
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
