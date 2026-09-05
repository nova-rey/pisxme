"""Co-locate the LM74700 gate FETs with their controllers and route gates."""
from pathlib import Path
import pcbnew
ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'PHASE21_CONTROLS_REGULATOR_CONTROLS.kicad_pcb'
OUTPUT=ROOT/'PHASE21_CONTROLS_REGULATOR_CONTROLS_GATES.kicad_pcb'
def P(x,y): return pcbnew.VECTOR2I_MM(x,y)
def tr(b,n,a,z,l=pcbnew.F_Cu,w=.20):
 t=pcbnew.PCB_TRACK(b);t.SetStart(P(*a));t.SetEnd(P(*z));t.SetLayer(l);t.SetWidth(pcbnew.FromMM(w));t.SetNet(n);b.Add(t)
def via(b,n,xy):
 v=pcbnew.PCB_VIA(b);v.SetPosition(P(*xy));v.SetWidth(pcbnew.FromMM(.55));v.SetDrill(pcbnew.FromMM(.30));v.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);v.SetNet(n);b.Add(v)
def fp(b,r): return next(f for f in b.GetFootprints() if f.GetReference()==r)
def main():
 b=pcbnew.LoadBoard(str(INPUT)); ga=b.FindNet('/POWER_INPUT/GATE_A'); gb=b.FindNet('/POWER_INPUT/GATE_B'); assert ga and gb
 q1=fp(b,'Q1');q2=fp(b,'Q2');q1.SetPosition(P(30,78));q2.SetPosition(P(10,108));q1.SetOrientationDegrees(0);q2.SetOrientationDegrees(0)
 # Each gate leaves U1/U2 on F.Cu, takes a single ordinary via, then runs on
 # B.Cu to the relocated FET gate and returns with a short dogbone.
 tr(b,ga,(19.5,76.45),(19.5,74.5));tr(b,ga,(19.5,74.5),(24,74.5));via(b,ga,(24,74.5));tr(b,ga,(24,74.5),(32.54,74.5),pcbnew.B_Cu);via(b,ga,(32.54,74.5));tr(b,ga,(32.54,74.5),(32.54,78))
 tr(b,gb,(19.5,96.45),(19.5,98.5));tr(b,gb,(19.5,98.5),(14,98.5));via(b,gb,(14,98.5));tr(b,gb,(14,98.5),(12.54,98.5),pcbnew.B_Cu);tr(b,gb,(12.54,98.5),(12.54,108),pcbnew.B_Cu);via(b,gb,(12.54,108))
 b.Save(str(OUTPUT));print(OUTPUT)
if __name__=='__main__':main()
