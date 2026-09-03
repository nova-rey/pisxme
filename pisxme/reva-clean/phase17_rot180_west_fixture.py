"""Disposable Phase 17 experiment: 180-degree CM5IO ESD orientation."""
from pathlib import Path
import os
import pcbnew

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'CM5IO_ROT180_WEST_FIXTURE.kicad_pcb'
NETS=['CM5_GBE_TD0_P','CM5_GBE_TD0_N','CM5_GBE_TD1_P','CM5_GBE_TD1_N',
      'CM5_GBE_TD2_P','CM5_GBE_TD2_N','CM5_GBE_TD3_P','CM5_GBE_TD3_N']
def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def add(b,n,pts,layer=pcbnew.F_Cu):
    for a,z in zip(pts,pts[1:]):
        t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z));
        t.SetLayer(layer); t.SetWidth(pcbnew.FromMM(.127)); t.SetNet(n); b.Add(t)
def via(b,n,p):
    q=pcbnew.PCB_VIA(b); q.SetPosition(V(*p)); q.SetWidth(pcbnew.FromMM(.45)); q.SetDrill(pcbnew.FromMM(.20)); q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNet(n); b.Add(q)
def main():
    b=pcbnew.NewBoard('')
    b.SetCopperLayerCount(6)
    for layer,name in ((pcbnew.F_Cu,'F.Cu'),(pcbnew.In1_Cu,'In1.GND'),(pcbnew.In2_Cu,'In2.PWR'),(pcbnew.In3_Cu,'In3.PWR12V'),(pcbnew.In4_Cu,'In4.GND'),(pcbnew.B_Cu,'B.Cu')): b.SetLayerName(layer,name)
    nets={}
    for name in NETS:
        nets[name]=pcbnew.NETINFO_ITEM(b,name); b.Add(nets[name])
    lib=ROOT/'PiSXMe_RevA_Clean.pretty'
    def load(name,ref):
        f=pcbnew.PCB_IO_KICAD_SEXPR().FootprintLoad(str(lib),name)
        if f is None: raise RuntimeError('missing footprint '+name)
        f.SetReference(ref); b.Add(f); return f
    j7=load('PiSXMeRevAClean_Raspberry_Pi_5_Compute_Module','J7')
    u9=load('USON-10_2.5x1.0mm_P0.5mm','U9')
    u6=load('USON-10_2.5x1.0mm_P0.5mm','U6')
    j2=load('EDAC_A70_112_331N126','J2')
    j2rot=0 if os.environ.get('PISXME_LAYER_SPLIT')=='1' else 180
    for f,p,r in ((j7,(35,130),0),(u9,(24,68),180),(u6,(30,68),180),(j2,(24,45),j2rot)):
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
    if os.environ.get('PISXME_LAYER_SPLIT')!='1':
        for name,(p,f,pad) in src.items(): add(b,nets[name],p+[tuple(q/1e6 for q in f.FindPadByNumber(pad).GetPosition())])
    else:
        # TD3 and TD1 stay F.Cu; TD2 and TD0 use B.Cu to clear the
        # interleaved J7 pad field. Every transition is outside a pad.
        split={
          'CM5_GBE_TD3_P':('F',(30.0,99.1),(24.0,67.0)),
          'CM5_GBE_TD3_N':('F',(30.5,99.5),(24.5,67.5)),
          'CM5_GBE_TD2_N':('B',(30.0,100.3),(25.0,68.5)),
          'CM5_GBE_TD2_P':('B',(30.8,100.7),(25.8,69.0)),
          'CM5_GBE_TD1_P':('B',(38.0,99.1),(31.5,67.0)),
          'CM5_GBE_TD1_N':('B',(38.8,99.5),(32.3,67.5)),
          'CM5_GBE_TD0_N':('B',(39.6,100.3),(33.1,68.5)),
          'CM5_GBE_TD0_P':('B',(40.4,100.7),(33.9,69.0))}
        for name,(p,f,pad) in src.items():
            layer,sv,ev=split[name]; ep=tuple(q/1e6 for q in f.FindPadByNumber(pad).GetPosition())
            add(b,nets[name],[p[0],sv],pcbnew.F_Cu); via(b,nets[name],sv)
            add(b,nets[name],[sv,ev],pcbnew.B_Cu); via(b,nets[name],ev)
            add(b,nets[name],[ev,ep],pcbnew.F_Cu)
    # Connector-side launch from the opposite ESD pads into the 180-degree
    # MagJack. These are explicit monotonic pair corridors, not copied rows.
    dst={
      'CM5_GBE_TD3_P':(u9,'6',(19.555,53.89)), 'CM5_GBE_TD3_N':(u9,'7',(18.285,51.35)),
      'CM5_GBE_TD2_N':(u9,'9',(20.825,51.35)), 'CM5_GBE_TD2_P':(u9,'10',(22.095,53.89)),
      'CM5_GBE_TD1_P':(u6,'5',(27.175,53.89)), 'CM5_GBE_TD1_N':(u6,'4',(23.365,51.35)),
      'CM5_GBE_TD0_N':(u6,'2',(28.445,51.35)), 'CM5_GBE_TD0_P':(u6,'1',(29.715,53.89))}
    if os.environ.get('PISXME_LAYER_SPLIT')=='1':
        dst={
          'CM5_GBE_TD3_P':(u9,'6',(28.445,36.11)), 'CM5_GBE_TD3_N':(u9,'7',(29.715,38.65)),
          'CM5_GBE_TD2_N':(u9,'9',(27.175,38.65)), 'CM5_GBE_TD2_P':(u9,'10',(25.905,36.11)),
          'CM5_GBE_TD1_P':(u6,'5',(20.825,36.11)), 'CM5_GBE_TD1_N':(u6,'4',(24.635,38.65)),
          'CM5_GBE_TD0_N':(u6,'2',(19.555,38.65)), 'CM5_GBE_TD0_P':(u6,'1',(18.285,36.11))}
    lanes={
      'CM5_GBE_TD3_P':[(23.615,67.0),(16.0,67.0),(16.0,54.5)],
      'CM5_GBE_TD3_N':[(23.615,67.5),(16.5,67.5),(16.5,53.5)],
      'CM5_GBE_TD2_N':[(23.615,68.5),(17.0,68.5),(17.0,52.5)],
      'CM5_GBE_TD2_P':[(23.615,69.0),(17.5,69.0),(17.5,51.5)],
      'CM5_GBE_TD1_P':[(29.615,67.0),(31.0,67.0),(31.0,54.5)],
      'CM5_GBE_TD1_N':[(29.615,67.5),(31.5,67.5),(31.5,53.5)],
      'CM5_GBE_TD0_N':[(29.615,68.5),(32.0,68.5),(32.0,52.5)],
      'CM5_GBE_TD0_P':[(29.615,69.0),(32.5,69.0),(32.5,51.5)]}
    if os.environ.get('PISXME_LAYER_SPLIT')!='1':
        for name,(f,pad,end) in dst.items(): add(b,nets[name],lanes[name]+[end])
    else:
        # Use F.Cu for TD3/TD1 and B.Cu for TD2/TD0; through-hole MagJack
        # pads accept either layer directly.
        for name,(f,pad,end) in dst.items():
            layer=pcbnew.B_Cu if ('TD2_' in name or 'TD0_' in name) else pcbnew.F_Cu
            start=tuple(q/1e6 for q in f.FindPadByNumber('6' if name=='CM5_GBE_TD3_P' else '7' if name=='CM5_GBE_TD3_N' else '9' if name=='CM5_GBE_TD2_N' else '10' if name=='CM5_GBE_TD2_P' else '5' if name=='CM5_GBE_TD1_P' else '4' if name=='CM5_GBE_TD1_N' else '2' if name=='CM5_GBE_TD0_N' else '1').GetPosition())
            if layer==pcbnew.F_Cu: add(b,nets[name],lanes[name]+[end],layer)
            else:
                ev=(start[0]-0.9,start[1])
                add(b,nets[name],[start,ev],pcbnew.F_Cu); via(b,nets[name],ev)
                add(b,nets[name],[ev]+lanes[name][1:]+[end],layer)
    b.Save(str(OUT)); print('saved',OUT)
if __name__=='__main__': main()
