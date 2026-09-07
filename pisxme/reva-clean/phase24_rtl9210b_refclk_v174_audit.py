"""Native saved-connectivity audit for translated V174 REFCLK."""
from pathlib import Path
import tempfile
import pcbnew
HERE=Path(__file__).resolve().parent
PCB=HERE/'PHASE24_RTL9210B_REFCLK_SUPPORT_RELOCATED_V174.kicad_pcb'
P={('U1','61'),('J1','55')}; N={('U1','62'),('J1','53')}
def key(x): return (x.GetParentFootprint().GetReference(),x.GetNumber())
def got(b,ref,num):
 b.BuildConnectivity();p=b.FindFootprintByReference(ref).FindPadByNumber(num)
 return {key(x) for x in b.GetConnectivity().GetConnectedItems(p) if type(x).__name__=='PAD'}
def main():
 b=pcbnew.LoadBoard(str(PCB));assert P<=got(b,'U1','61');assert N<=got(b,'U1','62')
 bad=pcbnew.LoadBoard(str(PCB));victim=next(x for x in bad.GetTracks() if type(x).__name__=='PCB_TRACK' and x.GetNetname()=='REFCLK_P');bad.RemoveNative(victim)
 with tempfile.NamedTemporaryFile(suffix='.kicad_pcb') as f:
  bad.Save(f.name);q=pcbnew.LoadBoard(f.name);assert not(P<=got(q,'U1','61'))
 print('V174 native REFCLK connectivity PASS; trace-removal negative control PASS')
if __name__=='__main__':main()
