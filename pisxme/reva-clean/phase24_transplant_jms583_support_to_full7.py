"""Transplant the verified JMS583 support-field primitive onto FULL7."""
from pathlib import Path
import os
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / os.environ.get('P24_SUPPORT_BASE', 'PHASE24_DUAL_MODE_STORAGE_NC39_USB3_FULL7.kicad_pcb')
DONOR = R / os.environ.get('P24_SUPPORT_DONOR', 'PHASE24_DUAL_MODE_STORAGE_NC39_QFN_ESCAPE_REPAIR_V3.kicad_pcb')
OUT = R / os.environ.get('P24_SUPPORT_OUT', 'PHASE24_DUAL_MODE_STORAGE_FULL7_SUPPORT_PRIMITIVE.kicad_pcb')
SUPPORT = {'JMS_REXT','LXO','JMS_VDDREG_5V','XIN','XOUT','JMS_RESET_N',
           'JMS_AVDD33','JMS_AVDDL','JMS_VCCO','JMS_VCCK','JMS_XAVDDH'}
PARTS = ('C80','C81','C82','C83','C84','C85','R80','R81','R83','L10','Y10')
def V(q): return pcbnew.VECTOR2I_MM(float(q[0]), float(q[1]))
def xy(q): return pcbnew.ToMM(q.x), pcbnew.ToMM(q.y)

b = pcbnew.LoadBoard(str(BASE)); d = pcbnew.LoadBoard(str(DONOR))
bu = b.FindFootprintByReference('U11').GetPosition()
du = d.FindFootprintByReference('U11').GetPosition()
def T(q): return pcbnew.VECTOR2I(q.x + bu.x - du.x, q.y + bu.y - du.y)
for ref in PARTS:
    src, dst = d.FindFootprintByReference(ref), b.FindFootprintByReference(ref)
    dst.SetPosition(T(src.GetPosition())); dst.SetOrientationDegrees(src.GetOrientationDegrees())
for item in list(b.GetTracks()):
    if item.GetNetname() in SUPPORT: b.RemoveNative(item)
for item in d.GetTracks():
    if item.GetNetname() not in SUPPORT: continue
    n = b.FindNet(item.GetNetname())
    if isinstance(item, pcbnew.PCB_VIA):
        q = pcbnew.PCB_VIA(b); q.SetPosition(T(item.GetPosition())); q.SetWidth(item.GetWidth(pcbnew.F_Cu)); q.SetDrill(item.GetDrill()); q.SetLayerPair(item.TopLayer(), item.BottomLayer())
    else:
        q = pcbnew.PCB_TRACK(b); q.SetStart(T(item.GetStart())); q.SetEnd(T(item.GetEnd())); q.SetLayer(item.GetLayer()); q.SetWidth(item.GetWidth())
    q.SetNet(n); q.SetNetCode(n.GetNetCode()); b.Add(q)
b.BuildListOfNets(); b.Save(str(OUT)); print(OUT)
