"""Restore Phase 16 non-Ethernet copper onto the corrected clean board."""
from pathlib import Path
import os, json, pcbnew
ROOT=Path(__file__).resolve().parent
BASE=Path(os.environ.get('PISXME_BASE', ROOT/'ACREAGE_EDAC_CORRECTED_PHASE17.kicad_pcb'))
SNAP=Path(os.environ.get('PISXME_SNAPSHOT', ROOT/'phase16_copper_snapshot.json'))
OUT=Path(os.environ.get('PISXME_OUT', ROOT/'ACREAGE_PHASE16_CM5IO_EDAC_PHASE17.kicad_pcb'))
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def short(s): return str(s).rsplit('/',1)[-1]
def main():
 rows=json.loads(SNAP.read_text()); b=pcbnew.LoadBoard(str(BASE))
 for row in rows:
  # The corrected source netlist is the authority for the power islands.  Do
  # not transplant stale Phase-16 regulator/power copper while rebuilding a
  # local island; PCIe and other signal copper remain reusable.
  if (str(row['net']).startswith(('/REGULATORS/', '/POWER_INPUT/')) or
      short(row['net']) in ('POWER_GND', '12V_PROTECTED')):
   continue
  n=short(row['net'])
  if not n or n.startswith('CM5_GBE_TD'): continue
  target=b.FindNet(row['net']) or b.FindNet(n) or b.FindNet('/'+n)
  if target is None: continue
  if row['kind']=='via':
   q=pcbnew.PCB_VIA(b);q.SetPosition(V(*row['p']));q.SetWidth(pcbnew.FromMM(row['w']));q.SetDrill(pcbnew.FromMM(row['d']));q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);q.SetNetCode(target.GetNetCode());b.Add(q)
  else:
   q=pcbnew.PCB_TRACK(b);q.SetStart(V(*row['a']));q.SetEnd(V(*row['z']));q.SetLayer(row['layer']);q.SetWidth(pcbnew.FromMM(row['w']));q.SetNetCode(target.GetNetCode());b.Add(q)
 b.Save(str(OUT));print('saved',OUT)
if __name__=='__main__': main()
