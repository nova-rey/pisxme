"""Promote the clean coordinated Phase 19 storage island into the V5 board."""
from pathlib import Path
import pcbnew

R = Path(__file__).resolve().parent
BASE = R / "PHASE23_TEST_DEBUG_PADS_V5.kicad_pcb"
DONOR = R / "PHASE19_RELOC_U270J190_COORD49_FULL.kicad_pcb"
OUT = R / "PHASE24_COORDINATED_STORAGE_EXPANDED.kicad_pcb"
SHIFT = (0.0, 80.0)
STORAGE_REFS = ("U7", "J3", "C30", "C31", "C32", "C33", "Y1", "R23", "C42", "C43")
def canon(name):
    return "/CORE_CM5/" + name if name.startswith("CM5_USB3_") else name

def mm(v): return pcbnew.FromMM(v)
def xy(p): return pcbnew.ToMM(p.GetPosition().x), pcbnew.ToMM(p.GetPosition().y)
def shift_pos(p): return pcbnew.VECTOR2I_MM(pcbnew.ToMM(p.x) + SHIFT[0], pcbnew.ToMM(p.y) + SHIFT[1])
def shift_xy(p): return (p[0] + SHIFT[0], p[1] + SHIFT[1])
def expand_outline(board, drawings):
    for d in drawings:
        if d.GetLayer() == pcbnew.Edge_Cuts:
            board.RemoveNative(d)
    for a,z in [((0,0),(300,280)),((300,280),(300,0)),((300,0),(0,0)),((0,280),(300,280))]:
        s=pcbnew.PCB_SHAPE(board); s.SetShape(pcbnew.SHAPE_T_SEGMENT); s.SetStart(pcbnew.VECTOR2I_MM(*a)); s.SetEnd(pcbnew.VECTOR2I_MM(*z)); s.SetLayer(pcbnew.Edge_Cuts); s.SetWidth(mm(.05)); board.Add(s)

def main():
    target = pcbnew.LoadBoard(str(BASE)); donor = pcbnew.LoadBoard(str(DONOR))
    edge_drawings = [d for d in target.GetDrawings() if d.GetLayer() == pcbnew.Edge_Cuts]
    donor_meta = {}
    for ref in STORAGE_REFS:
        src = donor.FindFootprintByReference(ref)
        if src is not None:
            donor_meta[ref] = (src.GetPosition(), src.GetOrientationDegrees(), src.GetLayer(), {str(p.GetNumber()): canon(p.GetNetname()) for p in src.Pads()})
    donor_tracks = []
    for item in donor.GetTracks():
        raw_name = item.GetNetname()
        if not any(x in raw_name for x in ("USB3", "SATA", "BRIDGE_XI", "BRIDGE_XO", "VSSOSC")): continue
        name = canon(raw_name)
        if isinstance(item, pcbnew.PCB_VIA): donor_tracks.append(("via", name, item.GetPosition()))
        else: donor_tracks.append(("track", name, item.GetStart(), item.GetEnd(), item.GetLayer(), item.GetWidth()))
    names = {x[1] for x in donor_tracks}
    nets = {}
    next_code = max((n.GetNetCode() for n in target.GetNetsByName().values()), default=0) + 1
    for name in sorted(names):
        n = target.FindNet(name)
        if n is None:
            n = pcbnew.NETINFO_ITEM(target, name); n.SetNetCode(next_code); next_code += 1; target.Add(n)
        nets[name] = n
    # Remove only target storage footprints and all copper on the affected
    # high-speed/clock nets.  The rest of the Phase 23/24 board is retained.
    io = pcbnew.PCB_IO_KICAD_SEXPR()
    for ref in STORAGE_REFS:
        if ref not in donor_meta: continue
        src_pos, src_rot, src_layer, src_pads = donor_meta[ref]
        f = target.FindFootprintByReference(ref)
        if f is None:
            f = io.FootprintLoad(str(R / "PiSXMe_RevA_Clean.pretty"), {
                "U7":"TUSB9261IPVP_HTQFP64", "J3":"JAE_SM3ZS067U410ABR1000_BKEY",
                "C30":"C_0402_1005Metric", "C31":"C_0402_1005Metric",
                "C32":"C_0402_1005Metric", "C33":"C_0402_1005Metric",
                "Y1":"Crystal_3225_4Pad", "R23":"R_0402_1005Metric",
                "C42":"C_0402_1005Metric", "C43":"C_0402_1005Metric"}[ref])
            f.SetReference(ref); target.Add(f)
        if not hasattr(f, "SetReference"):
            raise RuntimeError(f"footprint load failed for {ref}: {type(f)}")
        f.SetReference(ref); f.SetPosition(shift_pos(src_pos)); f.SetOrientationDegrees(src_rot); f.SetLayer(src_layer)
        for p in f.Pads():
            name = src_pads.get(str(p.GetNumber()), "")
            if name:
                n = nets.get(name) or target.FindNet(name)
                if n is not None: p.SetNet(n); p.SetNetCode(n.GetNetCode())
    for t in list(target.GetTracks()):
        if t.GetNetname() in names: target.Remove(t)
    # Copy only selected donor copper, preserving the donor's validated
    # geometry and ordinary through-via policy.
    for item in donor_tracks:
        kind, name = item[0], item[1]
        if name not in nets: continue
        n = nets[name]
        if kind == "via":
            v = pcbnew.PCB_VIA(target); v.SetPosition(shift_pos(item[2])); v.SetWidth(mm(.5)); v.SetDrill(mm(.3)); v.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu); v.SetNet(n); target.Add(v)
        else:
            t = pcbnew.PCB_TRACK(target); t.SetStart(shift_pos(item[2])); t.SetEnd(shift_pos(item[3])); t.SetLayer(item[4]); t.SetWidth(item[5]); t.SetNet(n); target.Add(t)
    expand_outline(target, edge_drawings)
    target.Save(str(OUT)); print(OUT)

if __name__ == "__main__": main()
