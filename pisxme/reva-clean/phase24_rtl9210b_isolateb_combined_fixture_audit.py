"""Saved-board audit for the combined ISOLATEB support fixture."""
from pathlib import Path
import pcbnew
P=Path(__file__).resolve().parent/'PHASE24_RTL9210B_ISOLATEB_COMBINED_FIXTURE.kicad_pcb'
def pad(b,r,n): return b.FindFootprintByReference(r).FindPadByNumber(n)
def joined(b,a,z): b.BuildConnectivity(); return z in b.GetConnectivity().GetConnectedItems(a)
b=pcbnew.LoadBoard(str(P))
assert pad(b,'U1','12').GetNetname()=='ISOLATEB'
assert pad(b,'U3','1').GetNetname()=='ISOLATEB'
assert joined(b,pad(b,'U1','12'),pad(b,'U3','1'))
assert pad(b,'U3','2').GetNetname()==''
for a,z in [('5','7'),('6','8')]: assert joined(b,pad(b,'U3',a),pad(b,'U3',z))
for net,a,z in [('RTL_3V3',('U3','5'),('JIN','1')),('SSD_3V3',('U3','6'),('JOUT','1')),
                ('MIC2545_ILIM',('U3','4'),('R15','1')),('GND',('U3','3'),('JGND','1'))]:
    assert pad(b,*a).GetNetname()==net and pad(b,*z).GetNetname()==net
    assert joined(b,pad(b,*a),pad(b,*z)),net
n=pcbnew.LoadBoard(str(P)); victim=next(x for x in n.GetTracks() if x.GetNetname()=='ISOLATEB')
n.RemoveNative(victim); assert not joined(n,pad(n,'U1','12'),pad(n,'U3','1'))
print('ISOLATEB combined fixture native connectivity PASS; EN/IN/OUT/support negative controls PASS')
