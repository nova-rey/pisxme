from skidl import *

set_default_tool(KICAD10)

vcc = Net('VCC')
sig = Net('LED_SIG')
gnd = Net('GND')

j1 = Part('Connector_Generic', 'Conn_01x02', ref='J1', footprint='Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical')
r1 = Part('Device', 'R', ref='R1', value='1k', footprint='Resistor_SMD:R_0603_1608Metric')
d1 = Part('Device', 'LED', ref='D1', footprint='LED_SMD:LED_0603_1608Metric')
c1 = Part('Device', 'C', ref='C1', value='100nF', footprint='Capacitor_SMD:C_0603_1608Metric')
pf_v = Part('power', 'PWR_FLAG', ref='#FLG01')
pf_g = Part('power', 'PWR_FLAG', ref='#FLG02')

j1[1] += vcc
j1[2] += gnd
vcc += r1[1], c1[1]
pf_v[1] += vcc
r1[2] += sig
d1[1] += sig
d1[2] += gnd
c1[2] += gnd
pf_g[1] += gnd

generate_schematic(tool=KICAD10)
generate_netlist(tool=KICAD10, file_='golden_flat.net', do_backup=False)
generate_pcb(tool=KICAD10, file_='golden_flat.kicad_pcb', do_backup=False, fp_libs=[])
