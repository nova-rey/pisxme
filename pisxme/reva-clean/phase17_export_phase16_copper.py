"""Snapshot Phase 16 copper using stable net names, not KiCad net codes."""
from pathlib import Path
import json
import pcbnew
ROOT=Path(__file__).resolve().parent
SRC=ROOT/'ACREAGE_PCIE_PHASE16.kicad_pcb'; OUT=ROOT/'phase16_copper_snapshot.json'
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def main():
 b=pcbnew.LoadBoard(str(SRC)); rows=[]
 for t in b.GetTracks():
  n=str(t.GetNetname())
  if not n: continue
  if isinstance(t,pcbnew.PCB_VIA):
   x,y=xy(t.GetPosition()); rows.append({'kind':'via','net':n,'p':(x,y),'w':pcbnew.ToMM(t.GetWidth()),'d':pcbnew.ToMM(t.GetDrill())})
  else:
   rows.append({'kind':'track','net':n,'a':xy(t.GetStart()),'z':xy(t.GetEnd()),'layer':t.GetLayer(),'w':pcbnew.ToMM(t.GetWidth())})
 OUT.write_text(json.dumps(rows,sort_keys=True))
 print(f'exported {len(rows)} Phase 16 copper items')
if __name__=='__main__': main()
