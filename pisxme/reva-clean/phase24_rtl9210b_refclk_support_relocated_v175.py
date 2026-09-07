"""V175: restore translated V158 crystal copper on the clean V174 basis."""
from pathlib import Path
import pcbnew
HERE=Path(__file__).resolve().parent; SRC=HERE/'PHASE24_RTL9210B_LOWER_1V1_HANDOFF_V160.kicad_pcb'; BASE=HERE/'PHASE24_RTL9210B_REFCLK_SUPPORT_RELOCATED_V174.kicad_pcb'; OUT=HERE/'PHASE24_RTL9210B_REFCLK_SUPPORT_RELOCATED_V175.kicad_pcb'; F,B=pcbnew.F_Cu,pcbnew.B_Cu
DY=-8.
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def shift(q): return P(q.x/1e6,q.y/1e6+DY)
def copy_item(dst,src,item,net):
 if type(item).__name__=='PCB_VIA':
  q=pcbnew.PCB_VIA(dst);q.SetPosition(shift(item.GetPosition()));q.SetWidth(item.GetWidth());q.SetDrill(item.GetDrill());q.SetLayerPair(F,B)
 else:
  q=pcbnew.PCB_TRACK(dst);q.SetStart(shift(item.GetStart()));q.SetEnd(shift(item.GetEnd()));q.SetLayer(item.GetLayer());q.SetWidth(item.GetWidth())
 q.SetNet(net);q.SetNetCode(net.GetNetCode());dst.Add(q)
def main():
 dst=pcbnew.LoadBoard(str(BASE));src=pcbnew.LoadBoard(str(SRC)); names={'XTAL_IN','XTAL_OUT'}; nets={n:dst.FindNet(n) for n in names}
 for item in src.GetTracks():
  if item.GetNetname() not in names: continue
  pts=[item.GetPosition()] if type(item).__name__=='PCB_VIA' else [item.GetStart(),item.GetEnd()]
  if all(90<=p.x/1e6<=115 and 70<=p.y/1e6<=82 for p in pts): copy_item(dst,src,item,nets[item.GetNetname()])
 dst.BuildListOfNets();dst.Save(str(OUT));print(OUT)
if __name__=='__main__':main()
