#!/usr/bin/env python3
"""Generate a disposable native RTL9210B-to-M-key connectivity fixture."""
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
FP = HERE / "authority-inventory/rtl9210b/RTL9210B-CG_QUALIFICATION.kicad_mod"
OUT = HERE / "PHASE24_RTL9210B_NATIVE_FIXTURE.kicad_pcb"

legacy = FP.read_text()
pad_re = re.compile(r"\(pad (\d+) smd (?:oval|rect).*?\(at ([^ )]+) ([^ )]+) ([^ )]+)\).*?\(size ([^ )]+) ([^ )]+)\)", re.S)
u_pads = []
for m in pad_re.finditer(legacy):
    n, x, y, rot, sx, sy = m.groups()
    if n == "69":
        line = '(pad "69" smd rect (at 100 100) (size 4.8 4.8) (layers "F.Cu" "F.Paste" "F.Mask") (net 0 "GND"))'
    else:
        line = f'(pad "{n}" smd oval (at {float(x)+100:.3f} {float(y)+100:.3f} {rot}) (size {sx} {sy}) (layers "F.Cu" "F.Paste" "F.Mask") (net 0 ""))'
    u_pads.append((n, line))

m2 = {29:(137.75,94.725),31:(138.25,94.725),35:(139.25,94.725),37:(139.75,94.725),
      38:(140,102.275),41:(140.75,94.725),43:(141.25,94.725),47:(142.25,94.725),
      49:(142.75,94.725),50:(143,102.275),52:(143.5,102.275),53:(143.75,94.725),
      55:(144.25,94.725),69:(147.75,94.725)}
names = {29:"PCIE_RXN1",31:"PCIE_RXP1",35:"PCIE_TXN1",37:"PCIE_TXP1",38:"DEVSLP",
         41:"LANE0_RXN",43:"LANE0_RXP",47:"LANE0_TXN",49:"LANE0_TXP",50:"PERST_N",
         52:"CLKREQ_N",53:"REFCLK_N",55:"REFCLK_P",69:"PEDET"}
u_pin = {"64":"LANE0_RXP","65":"LANE0_RXN","67":"LANE0_TXN","68":"LANE0_TXP",
         "56":"PCIE_TXP1","57":"PCIE_TXN1","58":"PCIE_RXN1","59":"PCIE_RXP1",
         "61":"REFCLK_P","62":"REFCLK_N","8":"PEDET","13":"CLKREQ_N",
         "14":"PERST_N","26":"DEVSLP"}
net_id = {n:i+1 for i,n in enumerate(sorted(set(names.values())))}
net_id.update({"GND":0})
u = []
for n,line in u_pads:
    if n in u_pin:
        line = line.replace('(net 0 "")', f'(net {net_id[u_pin[n]]} "{u_pin[n]}")')
    u.append('    ' + line)
j = [f'    (pad "{n}" smd rect (at {x:.3f} {y:.3f}) (size .30 1.55) (layers "F.Cu" "F.Paste" "F.Mask") (net {net_id[names[n]]} "{names[n]}"))' for n,(x,y) in m2.items()]
tracks = []
for pin,net in u_pin.items():
    target = next(n for n,v in names.items() if v == net)
    ux,uy = next((float(re.search(r'\(at ([0-9.\-]+) ([0-9.\-]+)', line).group(1)), float(re.search(r'\(at ([0-9.\-]+) ([0-9.\-]+)', line).group(2))) for n,line in u_pads if n == pin)
    tx,ty = m2[target]
    tracks.append(f'  (segment (start {ux:.3f} {uy:.3f}) (end {tx:.3f} {ty:.3f}) (width .20) (layer "F.Cu") (net {net_id[net]}))')
layers = '''(layers (0 "F.Cu" signal) (2 "B.Cu" signal) (4 "In1.Cu" power "In1.GND") (6 "In2.Cu" power "In2.PWR") (8 "In3.Cu" power "In3.PROTECTED_12V") (10 "In4.Cu" power "In4.GND") (5 "F.SilkS" user "f.silkscreen") (7 "B.SilkS" user "b.silkscreen") (25 "Edge.Cuts" user))'''
nets = '\n'.join(f'  (net {i} "{name}")' for name,i in sorted(net_id.items(), key=lambda x:x[1]))
u_block = '\n'.join(['  (footprint "RTL9210B-CG_QUALIFICATION" (layer "F.Cu")', '    (property "Reference" "U1" (at 100 92 0) (layer "F.SilkS") (effects (font (size 1 1) (thickness .15))))', '    (property "Value" "RTL9210B-CG" (at 100 108 0) (layer "F.Fab") hide (effects (font (size 1 1))))', '    (attr smd)', *u, '  )'])
j_block = '\n'.join(['  (footprint "M2_MKEY_FIXTURE" (layer "F.Cu")', '    (property "Reference" "J1" (at 140 92 0) (layer "F.SilkS") (effects (font (size 1 1) (thickness .15))))', '    (property "Value" "M.2 M-key" (at 140 108 0) (layer "F.Fab") hide (effects (font (size 1 1))))', '    (attr smd)', *j, '  )'])
OUT.write_text('(kicad_pcb\n (version 20260206) (generator pcbnew)\n (general (thickness 1.6))\n (paper "A4")\n ' + layers + '\n (setup (pad_to_mask_clearance 0))\n' + nets + '\n' + u_block + '\n' + j_block + '\n' + '\n'.join(tracks) + '\n)\n')
print(OUT)
