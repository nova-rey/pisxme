"""Source-owned disposable rebuild of the mode jumper as J8.

The source XML owns the reference and nets; this helper only materializes the
missing footprint into a routed disposable board and then rewires its two
mode nets. It never changes the power-input J5.
"""
from pathlib import Path
import argparse, pcbnew
from phase3_scaffold import balanced
from phase24_place_dual_mode_storage_island import pcb_footprint, LIB
ap=argparse.ArgumentParser(); ap.add_argument('base'); ap.add_argument('output'); a=ap.parse_args()
R=Path(__file__).resolve().parent; text=(R/a.base).read_text()
mode=pcb_footprint(LIB/'MODE_JUMPER_1x04.kicad_mod','J8',260,165,
 {1:'FORCE_SATA',2:'AUTO_PEDET',3:'FORCE_NVME',4:'MODE_IN'})
text=text.rstrip(); assert text.endswith(')'); text=text[:-1]+'\n'+mode+'\n)\n'
tmp=R/(a.output+'.kicad_pcb'); tmp.write_text(text)
b=pcbnew.LoadBoard(str(tmp)); F=pcbnew.F_Cu
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def pad(ref,num): return b.FindFootprintByReference(ref).FindPadByNumber(str(num))
def xy(p): return pcbnew.ToMM(p.GetPosition().x),pcbnew.ToMM(p.GetPosition().y)
def tr(n,p,q):
 t=pcbnew.PCB_TRACK(b); t.SetStart(V(*p)); t.SetEnd(V(*q)); t.SetLayer(F); t.SetWidth(pcbnew.FromMM(.15)); t.SetNet(n); t.SetNetCode(n.GetNetCode()); b.Add(t)
for name in ('AUTO_PEDET','MODE_IN'):
 n=b.FindNet(name)
 for item in list(b.GetTracks()):
  if item.GetNetCode()==n.GetNetCode(): b.RemoveNative(item)
tr(b.FindNet('AUTO_PEDET'),xy(pad('J3',69)),xy(pad('J8',2)))
tr(b.FindNet('MODE_IN'),xy(pad('J8',4)),xy(pad('U14',2)))
b.BuildListOfNets(); b.Save(str(R/a.output)); tmp.unlink()
print(R/a.output)
