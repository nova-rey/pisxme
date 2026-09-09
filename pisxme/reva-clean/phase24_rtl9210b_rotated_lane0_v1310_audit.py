"""V1310 native saved-board lane audit with per-pair negative controls."""
from pathlib import Path
import pcbnew
PCB=Path(__file__).resolve().parent/'PHASE24_RTL9210B_ROTATED_LANE0_V1310.kicad_pcb'
P=[('64','43','LANE0_RXP'),('65','41','LANE0_RXN'),('67','47','LANE0_TXN'),('68','49','LANE0_TXP')]
def pads(b): return {(f.GetReference(),p.GetNumber()):p for f in b.GetFootprints() for p in f.Pads()}
def c(b,a,z):
    b.BuildConnectivity(); q=pads(b); return q[z] in b.GetConnectivity().GetConnectedItems(q[a])
b=pcbnew.LoadBoard(str(PCB)); assert all(c(b,('U1',u),('J1',j)) for u,j,_ in P)
for u,j,n in P:
    t=pcbnew.LoadBoard(str(PCB)); cohort=[q for q in t.GetTracks() if q.GetNetname()==n]
    assert cohort,n+' source cohort missing'
    for q in cohort:t.RemoveNative(q)
    assert not c(t,('U1',u),('J1',j)),n+' negative control did not fail'
print('PASS V1310 native four-pair endpoint connectivity; four source-cohort negative controls PASS')
