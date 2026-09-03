"""Machine-check the TI ESDS304DBVR package authority and disposable mapping."""
from pathlib import Path
import pcbnew

ROOT=Path(__file__).resolve().parent
EXPECTED={"1":(-1.30,-.95),"2":(-1.30,0.0),"3":(-1.30,.95),"4":(1.30,.475),"5":(1.30,-.475)}
MAP={"U9":{"1":"CM5_GBE_TD3_P","3":"CM5_GBE_TD3_N","4":"CM5_GBE_TD2_P","5":"CM5_GBE_TD2_N"},
     "U6":{"1":"CM5_GBE_TD1_P","3":"CM5_GBE_TD1_N","4":"CM5_GBE_TD0_P","5":"CM5_GBE_TD0_N"}}
def mm(v): return float(v)/1e6
def main():
    f=pcbnew.FootprintLoad(str(ROOT/'PiSXMe_RevA_Clean.pretty'),'ESDS304DBVR_SOT23_5')
    failures=[]
    for num,(x,y) in EXPECTED.items():
        p=f.FindPadByNumber(num); q=p.GetPosition()
        if abs(mm(q[0])-x)>1e-6 or abs(mm(q[1])-y)>1e-6: failures.append(f'pad {num} position')
        if abs(mm(p.GetSize()[0])-.6)>1e-6 or abs(mm(p.GetSize()[1])-1.1)>1e-6: failures.append(f'pad {num} size')
        if not p.IsOnLayer(pcbnew.F_Cu) or not p.IsOnLayer(pcbnew.F_Mask) or not p.IsOnLayer(pcbnew.F_Paste): failures.append(f'pad {num} layers')
    b=pcbnew.LoadBoard(str(ROOT/'ESDS304_ETHERNET_CLEAN_DISPOSABLE_FIXTURE.kicad_pcb'))
    required=set(MAP['U9'].values())|set(MAP['U6'].values())|{'/ETHERNET/ETH_GND'}
    present={n for n in required if b.FindNet(n) is not None}
    if present != required: failures.append('required nets missing')
    for ref,m in MAP.items():
        fp=b.FindFootprintByReference(ref)
        if fp is None: failures.append(ref+' missing'); continue
        for pad,n in m.items():
            if fp.FindPadByNumber(pad).GetNetname()!=n: failures.append(f'{ref}.{pad} mapping')
        if fp.FindPadByNumber('2').GetNetname()!='/ETHERNET/ETH_GND': failures.append(ref+'.2 ground')
    report=ROOT/'PHASE17_ESDS304_AUTHORITY_CHECK.md'
    status='PASS' if not failures else 'FAIL'
    report.write_text('# Phase 17 ESDS304 authority check\n\nStatus: `'+status+'`\n\n'
        '- TI DBV0005A exposed metal: 0.6 mm × 1.1 mm\n'
        '- TI pad arrangement: 1/2/3 left, 5/4 right; 2.6 mm row separation\n'
        '- Explicit F.Cu/F.Paste/F.Mask pads and project courtyard\n'
        '- Fixture mapping: U9/U6, all eight MDI nets, explicit ETH_GND\n\n'
        + ('No authority mismatches found.\n' if not failures else 'Failures: '+', '.join(failures)+'\n'))
    print(status, report)
    raise SystemExit(0 if not failures else 1)
if __name__=='__main__': main()
