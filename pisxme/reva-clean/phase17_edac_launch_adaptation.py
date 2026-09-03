"""Disposable pin-accurate EDAC launch adaptation of the CM5IO oracle."""
from pathlib import Path
import pcbnew

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'CM5IO_PISXME_ETHERNET_TRANSPLANT_FIXTURE.kicad_pcb'
OUT=ROOT/'CM5IO_EDAC_PIN_ACCURATE_LAUNCH_FIXTURE.kicad_pcb'

def V(x,y): return pcbnew.VECTOR2I_MM(x,y)
def xy(p): return pcbnew.ToMM(p.x),pcbnew.ToMM(p.y)
def addroute(b,pts,n,layer=pcbnew.F_Cu):
    for a,z in zip(pts,pts[1:]):
        t=pcbnew.PCB_TRACK(b); t.SetStart(V(*a)); t.SetEnd(V(*z)); t.SetLayer(layer)
        t.SetWidth(pcbnew.FromMM(.127)); t.SetNet(n); b.Add(t)
def addvia(b,p,n):
    q=pcbnew.PCB_VIA(b); q.SetPosition(V(*p)); q.SetWidth(pcbnew.FromMM(.45)); q.SetDrill(pcbnew.FromMM(.20))
    q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu); q.SetNet(n); b.Add(q)

def main():
    b=pcbnew.LoadBoard(str(BASE))
    j=b.FindFootprintByReference('J2')
    # Production EDAC authority: MDI is pads 1..8, center taps 9..12.
    net={n:b.FindNet(n) for n in ('CM5_GBE_TD0_P','CM5_GBE_TD0_N','CM5_GBE_TD1_P','CM5_GBE_TD1_N',
                                  'CM5_GBE_TD2_P','CM5_GBE_TD2_N','CM5_GBE_TD3_P','CM5_GBE_TD3_N')}
    for p,n in zip(range(1,9),('CM5_GBE_TD0_P','CM5_GBE_TD0_N','CM5_GBE_TD1_P','CM5_GBE_TD1_N',
                               'CM5_GBE_TD2_P','CM5_GBE_TD2_N','CM5_GBE_TD3_P','CM5_GBE_TD3_N')):
        next(pad for pad in j.Pads() if str(pad.GetNumber())==str(p)).SetNet(net[n])
    # Cut only the oracle's connector-side portions; retain the complete
    # CM5->ESD escape and regenerate the EDAC-side launch at real pad 1..8.
    for t in list(b.GetTracks()):
        if not t.GetNetname().startswith('CM5_GBE_TD'):
            b.Remove(t); continue
        ys=(pcbnew.ToMM(t.GetStart().y),pcbnew.ToMM(t.GetEnd().y))
        if min(ys)<64.5: b.Remove(t)
    paths={
      'CM5_GBE_TD0_P':[(77.1,65.6),(78.5,64.2),(78.5,61.89),(78.215,61.89)],
      'CM5_GBE_TD0_N':[(76.6,65.6),(76.0,64.2),(76.0,59.35),(76.945,59.35)],
      'CM5_GBE_TD1_P':[(75.1,65.6),(75.1,64.2),(75.675,61.89)],
      'CM5_GBE_TD1_N':[(75.6,65.6),(74.5,64.2),(74.405,59.35)],
      'CM5_GBE_TD2_P':[(71.1,65.6),(72.5,64.2),(73.135,61.89)],
      'CM5_GBE_TD2_N':[(70.6,65.6),(71.5,64.2),(71.865,59.35)],
      'CM5_GBE_TD3_P':[(69.1,65.6),(70.0,64.2),(70.595,61.89)],
      'CM5_GBE_TD3_N':[(69.6,65.6),(68.5,64.2),(69.325,59.35)],
    }
    # Connector-side layer-split trial: TD1 and TD3 leave the ESD package on
    # ordinary through-vias and use B.Cu to pass beneath the F.Cu pair lanes.
    split={'CM5_GBE_TD1_P':(74.7,66.8),'CM5_GBE_TD1_N':(76.2,66.8),
           'CM5_GBE_TD3_P':(68.7,66.8),'CM5_GBE_TD3_N':(70.2,66.8)}
    for n,p in split.items(): addvia(b,p,net[n])
    for n,pts in paths.items():
        if n in split:
            addroute(b,[pts[0],split[n]],net[n])
            addroute(b,[split[n],*pts[1:]],net[n],pcbnew.B_Cu)
        else: addroute(b,pts,net[n])
    b.Save(str(OUT)); print('saved',OUT)
if __name__=='__main__': main()
