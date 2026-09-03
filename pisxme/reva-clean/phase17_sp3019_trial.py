"""Disposable SP3019-04HTG geometry trial; never used as production input."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "ACREAGE_PCIE_PHASE16.kicad_pcb"
W = pcbnew.FromMM(0.13208)

def v(x, y): return pcbnew.VECTOR2I_MM(x, y)
def N(b, name): return b.FindNet(name)
def tr(b, a, z, name, layer, width=W):
    t = pcbnew.PCB_TRACK(b); t.SetStart(v(*a)); t.SetEnd(v(*z)); t.SetLayer(layer)
    t.SetWidth(width); t.SetNet(N(b, name)); b.Add(t)
def via(b, p, name):
    q = pcbnew.PCB_VIA(b); q.SetPosition(v(*p)); q.SetWidth(pcbnew.FromMM(.45)); q.SetDrill(pcbnew.FromMM(.25))
    q.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu); q.SetNet(N(b, name)); b.Add(q)

def sp3019(b, ref, x, y, nets):
    old = b.FindFootprintByReference(ref)
    b.Remove(old)
    f = pcbnew.FOOTPRINT(b); f.SetReference(ref); f.SetValue("SP3019-04HTG")
    f.SetPosition(v(x, y)); f.SetFPID(pcbnew.LIB_ID("PiSXMe_RevA_Clean", "SP3019_SOT23_6L"))
    # Manufacturer SOT23-6L bottom-view topology: I/O 1/3/4/6, GND 2, NC 5.
    xy = {"1":(-.95,-.95), "2":(-.95,0), "3":(-.95,.95),
          "4":(.95,.95), "5":(.95,0), "6":(.95,-.95)}
    for pn, (px, py) in xy.items():
        p = pcbnew.PAD(f); p.SetNumber(pn); p.SetAttribute(pcbnew.PAD_ATTRIB_SMD)
        p.SetShape(pcbnew.PAD_SHAPE_ROUNDRECT); p.SetSize(v(1.1,.6)); p.SetRoundRectRadiusRatio(0.2)
        p.SetPosition(v(x + px, y + py))
        layers = pcbnew.LSET()
        layers.AddLayer(pcbnew.F_Cu)
        p.SetLayerSet(layers)
        name = nets.get(pn)
        if name: p.SetNet(N(b,name))
        f.Add(p)
    b.Add(f); return f

def main():
    b = pcbnew.LoadBoard(str(INPUT))
    sp3019(b, "U9", 25, 100, {"1":"CM5_GBE_TD3_P", "3":"CM5_GBE_TD3_N", "4":"CM5_GBE_TD2_P", "6":"CM5_GBE_TD2_N", "2":"ETH_GND"})
    sp3019(b, "U6", 29, 106, {"1":"CM5_GBE_TD1_P", "3":"CM5_GBE_TD1_N", "4":"CM5_GBE_TD0_P", "6":"CM5_GBE_TD0_N", "2":"ETH_GND"})
    # Source escapes are deliberately short and split by signal layer.
    left = {
      "CM5_GBE_TD3_P":((32.96,99.10),(31.6,99.10),(24.05,99.05)),
      "CM5_GBE_TD3_N":((32.96,99.50),(31.2,99.50),(24.05,100.95)),
      "CM5_GBE_TD2_N":((32.96,100.30),(30.8,100.30),(25.95,99.05)),
      "CM5_GBE_TD2_P":((32.96,100.70),(30.4,100.70),(25.95,100.95)),}
    for i,(name, pts) in enumerate(left.items()):
        for a,z in zip(pts,pts[1:]): tr(b,a,z,name,pcbnew.F_Cu if i<2 else pcbnew.B_Cu)
        if i>=2: via(b,pts[-1],name)
    right = {
      "CM5_GBE_TD1_P":((36.04,99.10),(35.4,99.10),(27.05,105.05)),
      "CM5_GBE_TD1_N":((36.04,99.50),(34.9,99.50),(27.05,106.95)),
      "CM5_GBE_TD0_N":((36.04,100.30),(34.4,100.30),(29.95,105.05)),
      "CM5_GBE_TD0_P":((36.04,100.70),(33.9,100.70),(29.95,106.95)),}
    for name,pts in right.items():
        for a,z in zip(pts,pts[1:]): tr(b,a,z,name,pcbnew.B_Cu)
    out = ROOT / "ACREAGE_ETHERNET_TRIAL_SP3019.kicad_pcb"; b.Save(str(out)); print(out)
if __name__ == "__main__": main()
