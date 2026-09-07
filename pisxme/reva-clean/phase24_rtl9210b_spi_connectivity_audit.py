"""Native saved-board SPI endpoint audit for the channelized RTL9210B fixture."""
from pathlib import Path
import sys,pcbnew
ROOT=Path(__file__).resolve().parent
DEFAULT=ROOT/'PHASE24_RTL9210B_CHANNELIZED_FULL_SPI_V1.kicad_pcb'
TARGET={
 'SPISI':('U1.18','U2.5'),'SPICLK':('U1.19','U2.6'),
 'SPISO3':('U1.22','U2.7'),'SPISO':('U1.23','U2.2'),
 'SPICS':('U1.24','U2.1')}
def tok(p):return f'{p.GetParentFootprint().GetReference()}.{p.GetNumber()}'
def audit_board(b):
 b.BuildConnectivity(); c=b.GetConnectivity()
 pads={tok(p):p for f in b.GetFootprints() for p in f.Pads()}
 for net,ends in TARGET.items():
  for e in ends:
   if e not in pads:raise AssertionError(f'missing {e}')
   if str(pads[e].GetNetname())!=net:raise AssertionError(f'{e}: wrong net {pads[e].GetNetname()}')
  for e in ends:
   reached={tok(x) for x in c.GetConnectedItems(pads[e]) if type(x).__name__=='PAD'}|{e}
   if not set(ends)<=reached:raise AssertionError(f'{net} disconnected at {e}: {sorted(reached)}')
  print(f'{net}: PASS ({ends[0]} <-> {ends[1]})')
 print('RTL9210B SPI native endpoint connectivity: PASS')
 return b
def audit(path):
 return audit_board(pcbnew.LoadBoard(str(path)))
def negative(path):
 b=audit(path); b.BuildConnectivity(); pads={tok(p):p for f in b.GetFootprints() for p in f.Pads()}
 for net,ends in TARGET.items():
  for item in b.GetConnectivity().GetConnectedItems(pads[ends[0]]):
   if type(item).__name__!='PCB_TRACK':continue
   trial=pcbnew.LoadBoard(str(path)); victim=next((x for x in trial.GetTracks() if type(x).__name__=='PCB_TRACK' and x.GetNetname()==net and x.GetStart()==item.GetStart() and x.GetEnd()==item.GetEnd()),None)
   if victim is None:continue
   trial.RemoveNative(victim)
   try:audit_board(trial)
   except Exception:return {'removed_net':net,'trace_removal_fails':True}
   # Native audit above cannot see an in-memory board, so test connectivity directly.
   trial.BuildConnectivity();tc=trial.GetConnectivity();tp={tok(p):p for f in trial.GetFootprints() for p in f.Pads()}
   if not set(ends)<=({tok(x) for x in tc.GetConnectedItems(tp[ends[0]]) if type(x).__name__=='PAD'}|{ends[0]}):return {'removed_net':net,'trace_removal_fails':True}
 raise AssertionError('no necessary trace found')
if __name__=='__main__':
 p=Path(sys.argv[1]) if len(sys.argv)>1 else DEFAULT;audit(p)
 if len(sys.argv)>2 and sys.argv[2]=='--negative-controls':print('negative controls:',negative(p))
