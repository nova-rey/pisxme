#!/usr/bin/env python3
"""Read-only SI/fabrication metrics for the selected exact-head board."""
from pathlib import Path
import hashlib,json,re,sys,collections

def blocks(text, token):
    pos=0; needle='('+token
    while True:
        st=text.find(needle,pos)
        if st<0:return
        # no quoted-string guard needed for these top-level tokens
        depth=0; quote=False; esc=False; en=None
        for i in range(st,len(text)):
            c=text[i]
            if quote:
                if esc:esc=False
                elif c=='\\':esc=True
                elif c=='"':quote=False
                continue
            if c=='"':quote=True
            elif c=='(':depth+=1
            elif c==')':
                depth-=1
                if depth==0:en=i+1;break
        if en is None:raise ValueError('unbalanced '+token)
        yield text[st:en];pos=en

def atom(p,b,default=None):
    m=re.search(p,b,re.S);return m.group(1) if m else default

def net(b):
    return atom(r'\(net\s+"([^"]*)"',b,'')

def main(board,geom,drc,out):
    txt=Path(board).read_text(); g=json.loads(Path(geom).read_text()); d=json.loads(Path(drc).read_text())
    vias=[]
    for b in blocks(txt,'via'):
        size=atom(r'\(size\s+([0-9.]+)',b); drill=atom(r'\(drill\s+([0-9.]+)',b)
        layers=re.findall(r'\(layers\s+"([^"]+)"\s+"([^"]+)"\)',b)
        vias.append({'net':net(b),'size_mm':float(size),'drill_mm':float(drill),'layers':list(layers[0]) if layers else []})
    all_layers={x for v in vias for x in v['layers']}
    via_sizes=collections.Counter((v['size_mm'],v['drill_mm']) for v in vias)
    target_nets={
      'PCIe_90R':['CM5_PER0_P','CM5_PER0_N','CM5_PET0_P','CM5_PET0_N','V100_PET0_P','V100_PET0_N','CM5_REFCLK_P','CM5_REFCLK_N'],
      'USB3_90R':['CM5_USB3_RX_P','CM5_USB3_RX_N','CM5_USB3_TX_P','CM5_USB3_TX_N','USB_RXP1','USB_RXN1','USB_TXP1','USB_TXN1','JMS_USB3_TXP','JMS_USB3_TXN'],
      'USB2_90R':['SERVICE_USB2_DP','SERVICE_USB2_DM'],
    }
    target_report={}
    for cls,nets in target_nets.items():
      rows=[]
      for n in nets:
        x=g.get('net_summary',{}).get(n)
        rows.append({'net':n,'present':bool(x),'widths_mm':x.get('widths_mm',[]) if x else [],'layers':x.get('layers',[]) if x else [],'length_mm':x.get('length_mm',0.0) if x else 0.0,'vias':x.get('vias',0) if x else 0,'width_matches_released_0.13208':bool(x and x.get('widths_mm')==[0.13208])})
      target_report[cls]=rows
    result={
      'board_sha256':hashlib.sha256(Path(board).read_bytes()).hexdigest(),
      'geometry_sha256':hashlib.sha256(Path(geom).read_bytes()).hexdigest(),
      'toolchain':{'kicad':d.get('kicad_version'),'qualified_image':'pisxme-kicad-light:v1','image_digest':'sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9'},
      'native_drc':{'violations':len(d.get('violations',[])),'unconnected_items':len(d.get('unconnected_items',[])),'ignored_checks':d.get('ignored_checks',[]),'schematic_parity_items':len(d.get('schematic_parity',[])),'status':'OPEN'},
      'stack_layer_roles':{'declared_layers':g['layers'],'segments_by_layer':g['segments_by_layer'],'inner_layer_signal_segments':sum(g['segments_by_layer'].get(x,0) for x in ['In1.Cu','In2.Cu','In3.Cu','In4.Cu']),'zones':g['zones'],'status':'PASS_DESIGN_BASIS_ONLY'},
      'via_geometry':{'count':len(vias),'unique_size_drill_counts':{f'{a:.2f}/{b:.2f}mm':c for (a,b),c in sorted(via_sizes.items())},'layers':sorted(all_layers),'all_outer_F_to_B':all(v['layers']==['F.Cu','B.Cu'] for v in vias),'status':'UNPROVEN_ORDER_SPECIFIC_FAB_CLOSURE'},
      'controlled_interface_metrics':target_report,
      'return_reference':{'power_gnd_zone_layers':[z['layer'] for z in g['zones'] if z.get('net')=='POWER_GND'],'power_gnd_segment_count':g.get('net_summary',{}).get('POWER_GND',{}).get('segments',0),'power_gnd_via_count':g.get('net_summary',{}).get('POWER_GND',{}).get('vias',0),'inner_layer_signal_segments':0,'status':'UNPROVEN_NATIVE_REFILL_AND_TRANSITION_AUDIT_REQUIRED'},
      'acceptance_rows':{
        'layers_routes_impedance_return':'OPEN',
        'INV-STACKUP':'PASS_DESIGN_BASIS_ONLY',
        'INV-IMPEDANCE':'UNPROVEN_NO_ORDER_COUPON_OR_MEASUREMENT',
        'INV-FAB':'FAIL_CURRENT_DRC_AND_OUT_OF_SCOPE_GEOMETRY',
        'SI-FAB-REF-001':'UNPROVEN',
        'SI-FAB-NETCLASS-001':'FAIL_STORAGE_AND_SERVICE_HIGH_SPEED_WIDTHS_NOT_RELEASED_TARGET',
        'SI-FAB-VIA-001':'UNPROVEN_ORDER_AND_PACKAGE_OVERLAY',
        'SI-FAB-COUPON-001':'UNPROVEN_NO_ORDER_COUPON',
        'SI-FAB-RETURN-001':'UNPROVEN',
      },
      'scope':{'protected_bus':'FENCED; no edits or acceptance credit','non_protected':'metrics only; physical repairs remain separate','hardware_measurements':'none claimed'}
    }
    Path(out).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
if __name__=='__main__':main(*sys.argv[1:])
