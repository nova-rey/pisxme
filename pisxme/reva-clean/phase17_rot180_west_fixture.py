"""Disposable Phase 17 experiment: 180-degree CM5IO ESD orientation."""
from pathlib import Path
import pcbnew

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'ACREAGE_EDAC_CORRECTED_PHASE17.kicad_pcb'
OUT=ROOT/'CM5IO_ROT180_WEST_FIXTURE.kicad_pcb'
NETS=['CM5_GBE_TD0_P','CM5_GBE_TD0_N','CM5_GBE_TD1_P','CM5_GBE_TD1_N',
      'CM5_GBE_TD2_P','CM5_GBE_TD2_N','CM5_GBE_TD3_P','CM5_GBE_TD3_N']
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def add(b,n,pts):
    for a,z in zip(pts,pts[1:]):
        t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z));
        t.SetLayer(pcbnew.F_Cu); t.SetWidth(pcbnew.FromMM(.127)); t.SetNet(n); b.Add(t)
def main():
    b=pcbnew.LoadBoard(str(BASE))
    for t in list(b.Tracks()): b.Remove(t)
    for z in list(b.Zones()): b.Remove(z)
    nets={name:b.FindNet(name) for name in NETS}
    for name,n in nets.items():
        if n is None: raise RuntimeError('missing net '+name)
    j7=b.FindFootprintByReference('J7'); u9=b.FindFootprintByReference('U9')
    u6=b.FindFootprintByReference('U6'); j2=b.FindFootprintByReference('J2')
    for f,p,r in ((j7,(35,130),0),(u9,(24,68),180),(u6,(30,68),180),(j2,(24,45),180)):
        f.SetPosition(V(*p)); f.SetOrientationDegrees(r)
    j7map={'3':'CM5_GBE_TD3_P','4':'CM5_GBE_TD1_P','5':'CM5_GBE_TD3_N','6':'CM5_GBE_TD1_N',
           '9':'CM5_GBE_TD2_N','10':'CM5_GBE_TD0_N','11':'CM5_GBE_TD2_P','12':'CM5_GBE_TD0_P'}
    u9map={'1':'CM5_GBE_TD2_P','2':'CM5_GBE_TD2_N','4':'CM5_GBE_TD3_N','5':'CM5_GBE_TD3_P','6':'CM5_GBE_TD3_P','7':'CM5_GBE_TD3_N','9':'CM5_GBE_TD2_N','10':'CM5_GBE_TD2_P'}
    u6map={'1':'CM5_GBE_TD0_P','2':'CM5_GBE_TD0_N','4':'CM5_GBE_TD1_N','5':'CM5_GBE_TD1_P','6':'CM5_GBE_TD1_P','7':'CM5_GBE_TD1_N','9':'CM5_GBE_TD0_N','10':'CM5_GBE_TD0_P'}
    j2map={'1':'CM5_GBE_TD0_P','2':'CM5_GBE_TD0_N','3':'CM5_GBE_TD1_P','6':'CM5_GBE_TD1_N','7':'CM5_GBE_TD2_P','8':'CM5_GBE_TD2_N','9':'CM5_GBE_TD3_P','10':'CM5_GBE_TD3_N'}
    for f,m in ((j7,j7map),(u9,u9map),(u6,u6map),(j2,j2map)):
        for p,name in m.items(): f.FindPadByNumber(p).SetNet(nets[name])
    # J7-to-ESD source escape: left group uses west lanes, right group east.
    src={
      'CM5_GBE_TD3_P':([(32.96,99.10),(26.0,99.10),(26.0,67.0)],u9,'5'),
      'CM5_GBE_TD3_N':([(32.96,99.50),(26.5,99.50),(26.5,67.5)],u9,'4'),
      'CM5_GBE_TD2_N':([(32.96,100.30),(27.0,100.30),(27.0,68.5)],u9,'2'),
      'CM5_GBE_TD2_P':([(32.96,100.70),(27.5,100.70),(27.5,69.0)],u9,'1'),
      'CM5_GBE_TD1_P':([(36.04,99.10),(73.0,99.10),(73.0,67.0)],u6,'6'),
      'CM5_GBE_TD1_N':([(36.04,99.50),(73.5,99.50),(73.5,67.5)],u6,'7'),
      'CM5_GBE_TD0_N':([(36.04,100.30),(74.0,100.30),(74.0,68.5)],u6,'9'),
      'CM5_GBE_TD0_P':([(36.04,100.70),(74.5,100.70),(74.5,69.0)],u6,'10')}
    for name,(p,f,pad) in src.items(): add(b,nets[name],p+[tuple(q/1e6 for q in f.FindPadByNumber(pad).GetPosition())])
    # Connector-side launch from the opposite ESD pads into the 180-degree
    # MagJack. These are explicit monotonic pair corridors, not copied rows.
    dst={
      'CM5_GBE_TD3_P':(u9,'6',(19.555,53.89)), 'CM5_GBE_TD3_N':(u9,'7',(18.285,51.35)),
      'CM5_GBE_TD2_N':(u9,'9',(20.825,51.35)), 'CM5_GBE_TD2_P':(u9,'10',(22.095,53.89)),
      'CM5_GBE_TD1_P':(u6,'5',(27.175,53.89)), 'CM5_GBE_TD1_N':(u6,'4',(23.365,51.35)),
      'CM5_GBE_TD0_N':(u6,'2',(28.445,51.35)), 'CM5_GBE_TD0_P':(u6,'1',(29.715,53.89))}
    lanes={
      'CM5_GBE_TD3_P':[(23.615,67.0),(16.0,67.0),(16.0,54.5)],
      'CM5_GBE_TD3_N':[(23.615,67.5),(16.5,67.5),(16.5,53.5)],
      'CM5_GBE_TD2_N':[(23.615,68.5),(17.0,68.5),(17.0,52.5)],
      'CM5_GBE_TD2_P':[(23.615,69.0),(17.5,69.0),(17.5,51.5)],
      'CM5_GBE_TD1_P':[(29.615,67.0),(31.0,67.0),(31.0,54.5)],
      'CM5_GBE_TD1_N':[(29.615,67.5),(31.5,67.5),(31.5,53.5)],
      'CM5_GBE_TD0_N':[(29.615,68.5),(32.0,68.5),(32.0,52.5)],
      'CM5_GBE_TD0_P':[(29.615,69.0),(32.5,69.0),(32.5,51.5)]}
    for name,(f,pad,end) in dst.items(): add(b,nets[name],lanes[name]+[end])
    b.Save(str(OUT)); print('saved',OUT)
if __name__=='__main__': main()
