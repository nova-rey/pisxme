"""Export official CM5IO MDI vectors before a second-board pcbnew load."""
from pathlib import Path
import json
import pcbnew

ROOT=Path(__file__).resolve().parent
SRC=ROOT/'CM5IO_PISXME_ETHERNET_TRANSPLANT_FIXTURE.kicad_pcb'
OUT=ROOT/'cm5io_mdi_geometry.json'
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def main():
    b=pcbnew.LoadBoard(str(SRC)); rows=[]
    for t in b.GetTracks():
        n=str(t.GetNetname()).rsplit('/',1)[-1]
        if n.startswith('CM5_GBE_TD'):
            rows.append({'net':n,'a':xy(t.GetStart()),'z':xy(t.GetEnd()),
                         'layer':t.GetLayer(),'width':pcbnew.ToMM(t.GetWidth())})
    OUT.write_text(json.dumps(rows,sort_keys=True,indent=2)+'\n')
    print(f'exported {len(rows)} official MDI segments to {OUT}')
if __name__=='__main__': main()
