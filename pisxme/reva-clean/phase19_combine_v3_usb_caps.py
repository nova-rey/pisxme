"""Combine the proven V3 USB3 schedule with the clean split-SATA launch."""
from pathlib import Path
import pcbnew

R=Path(__file__).resolve().parent
BASE=R/'ACREAGE_PHASE19_STORAGE_V3_USB_REGEN_V4.kicad_pcb'
DONOR=R/'PHASE19_V3_CAP_USB_CANDIDATE_REFILL.kicad_pcb'
OUT=R/'PHASE19_V3_USB_PROVEN_SPLIT_SATA.kicad_pcb'
V=lambda x,y: pcbnew.VECTOR2I_MM(x,y)

def main():
    b=pcbnew.LoadBoard(str(BASE)); d=pcbnew.LoadBoard(str(DONOR))
    find=lambda board,ref: next(f for f in board.GetFootprints() if f.GetReference()==ref)
    # Capture donor SATA copper before mutating the target.  Recreate objects
    # against target net objects, avoiding SWIG ownership/proxy aliasing.
    sata=[]
    for t in d.GetTracks():
        if not (t.GetNetname().startswith('/STORAGE/BRIDGE_SATA_') or
                t.GetNetname().startswith('/STORAGE/SATA_M2_')):
            continue
        if t.Type()==14:
            p=t.GetPosition(); sata.append(('V',t.GetNetname(),t.GetWidth(),t.GetDrill(),t.GetLayer(),p.x,p.y))
        else:
            sata.append(('T',t.GetNetname(),t.GetWidth(),t.GetLayer(),
                         t.GetStart().x,t.GetStart().y,t.GetEnd().x,t.GetEnd().y))
    # Replace the inherited C30-C33 regulator capacitors with the authoritative
    # 0402 inline capacitor footprints and preserve their donor placement.
    oldcaps={ref:find(b,ref) for ref in ('C30','C31','C32','C33')}
    j3=find(b,'J3')
    for old in oldcaps.values(): b.Remove(old)
    io=pcbnew.PCB_IO_KICAD_SEXPR()
    cap_xy={}
    caps={}
    for ref in ('C30','C31','C32','C33'):
        df=find(d,ref); p=df.GetPosition()
        cap_xy[ref]=(pcbnew.ToMM(p.x),pcbnew.ToMM(p.y))
        cap=io.FootprintLoad(str(R/'PiSXMe_RevA_Clean.pretty'),'C_0402_1005Metric')
        if cap is None: raise RuntimeError('cannot load 0402 footprint')
        cap.SetReference(ref); cap.SetPosition(V(*cap_xy[ref])); cap.SetOrientationDegrees(180); b.Add(cap); caps[ref]=cap
    # Materialize and reload newly added footprints before assigning nets;
    # KiCad 10 invalidates SWIG footprint proxies after board insertion.
    sync=R/'.phase19_combine_caps_sync.kicad_pcb'; b.Save(str(sync)); b=None; b=pcbnew.LoadBoard(str(sync))
    storage={}
    for name in ('SATA_M2_TX_P','SATA_M2_TX_N','SATA_M2_RX_P','SATA_M2_RX_N'):
        full='/STORAGE/'+name; n=b.FindNet(full)
        if n is None:
            n=pcbnew.NETINFO_ITEM(b,full); n.SetNetCode(b.GetNetCount()+len(storage)+1); b.Add(n)
        storage[full]=n
    links=(('BRIDGE_SATA_TX_P','SATA_M2_TX_P','C30','1','2'),
           ('BRIDGE_SATA_TX_N','SATA_M2_TX_N','C31','1','2'),
           ('BRIDGE_SATA_RX_P','SATA_M2_RX_P','C32','1','2'),
           ('BRIDGE_SATA_RX_N','SATA_M2_RX_N','C33','1','2'))
    # Assign all endpoint nets before removing donor SATA tracks.  KiCad 10
    # can invalidate footprint proxies during board collection mutation.
    for bridge_name,socket_name,ref,sockpad,bridgepad in links:
        bn=b.FindNet('/STORAGE/'+bridge_name); sn=storage['/STORAGE/'+socket_name]
        cf=b.FindFootprintByReference(ref)
        for num,n in ((sockpad,sn),(bridgepad,bn)):
            p=next(x for x in cf.Pads() if str(x.GetNumber())==num); p.SetNet(n); p.SetNetCode(n.GetNetCode())
        jp=next(x for x in b.FindFootprintByReference('J3').Pads() if str(x.GetNumber())==({'C30':'1','C31':'2','C32':'3','C33':'4'}[ref]))
        jp.SetNet(sn); jp.SetNetCode(sn.GetNetCode())
    targetnets={name:b.FindNet('/STORAGE/'+name) for name in
                ('BRIDGE_SATA_RX_N','BRIDGE_SATA_RX_P','BRIDGE_SATA_TX_N','BRIDGE_SATA_TX_P',
                 'SATA_M2_RX_N','SATA_M2_RX_P','SATA_M2_TX_N','SATA_M2_TX_P')}
    # Remove inherited direct SATA copper, leaving the proven USB3 copper.
    for t in list(b.GetTracks()):
        if t.GetNetname().startswith('/STORAGE/BRIDGE_SATA_') or t.GetNetname().startswith('/STORAGE/SATA_M2_'):
            b.Remove(t)
    # Copy the validated donor SATA routes, preserving width, layer and via
    # dimensions but attaching every object to the target net table.
    for row in sata:
        if row[0]=='V':
            _,name,w,drill,layer,x,y=row; n=targetnets[name.split('/')[-1]]; q=pcbnew.PCB_VIA(b);q.SetPosition(pcbnew.VECTOR2I(x,y));q.SetWidth(w);q.SetDrill(drill);q.SetLayerPair(pcbnew.F_Cu,pcbnew.B_Cu);q.SetNet(n);b.Add(q)
        else:
            _,name,w,layer,x,y,zx,zy=row; n=targetnets[name.split('/')[-1]]; q=pcbnew.PCB_TRACK(b);q.SetStart(pcbnew.VECTOR2I(x,y));q.SetEnd(pcbnew.VECTOR2I(zx,zy));q.SetLayer(layer);q.SetWidth(w);q.SetNet(n);b.Add(q)
    b.Save(str(OUT)); print(OUT)
if __name__=='__main__': main()
