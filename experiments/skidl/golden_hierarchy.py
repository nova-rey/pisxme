from skidl import *

set_default_tool(KICAD10)

vcc = Net('VCC')
gnd = Net('GND')
sig = Net('CHILD_SIG')

@subcircuit
def child(vcc, gnd, sig):
    r1 = Part('Device', 'R', ref='R1', value='1k', footprint='Resistor_SMD:R_0603_1608Metric')
    c1 = Part('Device', 'C', ref='C1', value='100nF', footprint='Capacitor_SMD:C_0603_1608Metric')
    r1[1] += vcc
    r1[2] += sig
    c1[1] += vcc
    c1[2] += gnd

child(vcc, gnd, sig)
j1 = Part('Connector_Generic', 'Conn_01x03', ref='J1', footprint='Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical')
j1[1] += vcc
j1[2] += sig
j1[3] += gnd
pf1 = Part('power', 'PWR_FLAG', ref='#FLG01')
pf2 = Part('power', 'PWR_FLAG', ref='#FLG02')
pf1[1] += vcc
pf2[1] += gnd

generate_schematic(tool=KICAD10)
generate_netlist(tool=KICAD10, file_='golden_hierarchy.net', do_backup=False)
