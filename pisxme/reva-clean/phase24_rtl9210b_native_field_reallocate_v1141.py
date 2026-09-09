"""V1141: native-board bounded QFN field reallocation from queried pad positions."""
from pathlib import Path
import pcbnew

H=Path(__file__).resolve().parent
BASE=H/'PHASE24_RTL9210B_QFN_GND_ATTACH_V1123.kicad_pcb'
OUT=H/'PHASE24_RTL9210B_NATIVE_FIELD_REALLOCATE_V1141.kicad_pcb'
F,B=pcbnew.F_Cu,pcbnew.B_Cu; W=pcbnew.FromMM(.20)
def P(x,y): return pcbnew.VECTOR2I_MM(float(x),float(y))
def XY(p): return (p.x/1e6,p.y/1e6)
def getpad(board,ref,name):
    f=next(f for f in board.GetFootprints() if f.GetReference()==ref)
    return next(p for p in f.Pads() if p.GetPadName()==name)
def tr(board,code,layer,points):
    for a,z in zip(points,points[1:]):
        q=pcbnew.PCB_TRACK(board); q.SetStart(P(*a)); q.SetEnd(P(*z)); q.SetLayer(layer)
        q.SetWidth(W); q.SetNetCode(code); board.Add(q)
def via(board,code,xy):
    q=pcbnew.PCB_VIA(board); q.SetPosition(P(*xy)); q.SetWidth(pcbnew.FromMM(.60)); q.SetDrill(pcbnew.FromMM(.30))
    q.SetLayerPair(F,B); q.SetNetCode(code); board.Add(q)
b=pcbnew.LoadBoard(str(BASE))
names=('RTL_3V3','RTL_1V1','RSET','GND','XTAL_IN','XTAL_OUT')
codes={n:b.FindNet(n).GetNetCode() for n in names}
# Clear signal copper through the native layer API, preserving board outline, pads, and net registry.
# This is a disposable local-field fixture; no production or remote copper is changed.
for layer in range(b.GetCopperLayerCount()):
    b.RemoveAllItemsOnLayer(layer)
def xy(ref,name): return XY(getpad(b,ref,name).GetPosition())
u51,u52,u53,u54,u55,u61,u62,u66=map(lambda n:xy('U1',n),('51','52','53','54','55','61','62','66'))
u45=xy('U1','45'); ep=xy('U1','69')
y1i,y1o,c1i,c2o,rset=xy('Y1','1'),xy('Y1','2'),xy('C1','1'),xy('C2','1'),xy('R1','1')
# Rail/RSET departures are allocated first, with ordinary through-vias.
tr(b,codes['RTL_3V3'],F,[u52,(u52[0]-1.0,u52[1]),(u52[0]-1.0,65.0)]); via(b,codes['RTL_3V3'],(u52[0]-1.0,65.0))
tr(b,codes['RTL_3V3'],B,[(u52[0]-1.0,65.0),(100.5,65.0),(100.5,64.0)])
tr(b,codes['RTL_1V1'],F,[u55,(u55[0]+1.0,u55[1])]); via(b,codes['RTL_1V1'],(u55[0]+1.0,u55[1]))
tr(b,codes['RTL_1V1'],B,[(u55[0]+1.0,u55[1]),(u55[0]+1.0,75.0),(102.5,75.0)])
tr(b,codes['RSET'],F,[rset,(rset[0]+6.0,rset[1]),(u51[0]+.75,64.0),u51])
# Native-query XTAL_IN upper departure and XTAL_OUT lower departure use separated B.Cu corridors.
tr(b,codes['XTAL_IN'],F,[u53,(u53[0]-1.0,u53[1]),(91.5,68.6)]); via(b,codes['XTAL_IN'],(91.5,68.6))
tr(b,codes['XTAL_IN'],B,[(91.5,68.6),(91.5,75.0),(85.5,75.0),(85.5,62.0)]); via(b,codes['XTAL_IN'],(85.5,62.0))
tr(b,codes['XTAL_IN'],F,[(85.5,62.0),c1i,y1i])
tr(b,codes['XTAL_OUT'],F,[u54,(u54[0]-1.0,u54[1]),(90.5,69.5)]); via(b,codes['XTAL_OUT'],(90.5,69.5))
tr(b,codes['XTAL_OUT'],B,[(90.5,69.5),(90.5,77.0),(83.5,77.0),(83.5,59.5)]); via(b,codes['XTAL_OUT'],(83.5,59.5))
tr(b,codes['XTAL_OUT'],F,[(83.5,59.5),(y1o[0],59.5),y1o,(90.0,59.0),(90.0,60.5),c2o])
# Preserve explicit source-to-exposed-pad GND attachment in this local proof.
tr(b,codes['GND'],F,[u45,ep]); tr(b,codes['GND'],F,[u66,ep])
b.BuildListOfNets(); pcbnew.ZONE_FILLER(b).Fill(b.Zones()); b.Save(str(OUT)); print(OUT)
print('native pads',u52,u53,u54,u55,y1i,y1o,c1i,c2o,rset)
