"""Create the first acreage USB3 routing candidate from the closed Phase 17 board."""
from pathlib import Path
import pcbnew

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "ACREAGE_PHASE17_COLOCATED_CT4_SPLIT.kicad_pcb"
OUT = ROOT / "ACREAGE_PHASE18_USB3_LOCAL.kicad_pcb"
WIDTH = pcbnew.FromMM(0.13208)  # 5.2 mil PiSXMe JLC 90-ohm basis


def mm(v):
    return pcbnew.FromMM(v)


def vec(x, y):
    return pcbnew.VECTOR2I(mm(x), mm(y))


def named_net(board, name):
    for candidate in (name, "/CORE_CM5/" + name, "/STORAGE/" + name):
        net = board.FindNet(candidate)
        if net:
            return net
    # The Phase 17 board predates the repaired storage child; materialize a
    # deterministic hierarchical net when a corrected storage name is new.
    candidate = "/STORAGE/" + name if name != "POWER_GND" else "POWER_GND"
    net = pcbnew.NETINFO_ITEM(board, candidate)
    board.Add(net)
    return net


def pad(fp, number):
    result = next((p for p in fp.Pads() if str(p.GetNumber()) == str(number)), None)
    if result is None:
        raise RuntimeError(f"missing {fp.GetReference()}.{number}")
    return result


def segment(board, net, start, end, layer):
    track = pcbnew.PCB_TRACK(board)
    track.SetStart(vec(*start))
    track.SetEnd(vec(*end))
    track.SetLayer(layer)
    track.SetWidth(WIDTH)
    track.SetNet(net)
    board.Add(track)


def transition(board, net, position):
    via = pcbnew.PCB_VIA(board)
    via.SetPosition(vec(*position))
    via.SetWidth(pcbnew.FromMM(0.50))
    via.SetDrill(pcbnew.FromMM(0.30))
    via.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
    via.SetNet(net)
    board.Add(via)


def main():
    board = pcbnew.LoadBoard(str(BASE))
    j7 = board.FindFootprintByReference("J7")
    u7 = board.FindFootprintByReference("U7")
    if not j7 or not u7:
        raise RuntimeError("J7/U7 missing")

    # Move only the storage bridge.  The acreage CM5, Ethernet and PCIe
    # placements/copper remain untouched.
    u7.SetPosition(vec(110, 105))
    u7.SetOrientationDegrees(180)

    # Materialize the corrected storage authority on the board before adding
    # USB3 copper; the Phase 17 ancestor still contains the old ordinal-pad
    # artifact on U7/J3.
    j3 = board.FindFootprintByReference("J3")
    if not j3:
        raise RuntimeError("J3 missing")
    storage_pads = (
        (u7, "57", "BRIDGE_SATA_TX_P"),
        (u7, "56", "BRIDGE_SATA_TX_N"),
        (u7, "60", "BRIDGE_SATA_RX_P"),
        (u7, "59", "BRIDGE_SATA_RX_N"),
        (u7, "24", "BRIDGE_3V3"),
        (u7, "41", "BRIDGE_1V1"),
        (u7, "4", "BRIDGE_RESET"),
        (u7, "21", "BRIDGE_CFG"),
        (j3, "1", "BRIDGE_SATA_TX_P"),
        (j3, "2", "BRIDGE_SATA_TX_N"),
        (j3, "3", "BRIDGE_SATA_RX_P"),
        (j3, "4", "BRIDGE_SATA_RX_N"),
        (j3, "5", "M2_3V3"),
        (j3, "6", "POWER_GND"),
    )
    for footprint, number, name in storage_pads:
        pad(footprint, number).SetNet(named_net(board, name))

    pairs = (
        ("CM5_USB3_RX_N", "128", "42"),
        ("CM5_USB3_RX_P", "130", "43"),
        ("CM5_USB3_TX_N", "140", "45"),
        ("CM5_USB3_TX_P", "142", "46"),
    )
    # Escape all four lanes around the existing PCIe breakout on B.Cu.  The
    # two via columns are outside J7/U7 pad fields and use 0.9/1.0 mm pitch;
    # this keeps the ordinary through-vias manufacturable and pair order
    # monotonic without plane-layer signals.
    via_columns = {
        "CM5_USB3_RX_N": ((72.0, 103.9), (103.0, 103.0)),
        "CM5_USB3_RX_P": ((72.0, 104.8), (103.0, 105.0)),
        "CM5_USB3_TX_N": ((72.0, 105.7), (103.0, 107.0)),
        "CM5_USB3_TX_P": ((72.0, 106.6), (103.0, 109.0)),
    }
    for name, source_pad, bridge_pad in pairs:
        net = named_net(board, name)
        source = pad(j7, source_pad)
        destination = pad(u7, bridge_pad)
        source.SetNet(net)
        destination.SetNet(net)
        if name.startswith("CM5_USB3_TX"):
            s = (pcbnew.ToMM(source.GetPosition().x), pcbnew.ToMM(source.GetPosition().y))
            d = (pcbnew.ToMM(destination.GetPosition().x), pcbnew.ToMM(destination.GetPosition().y))
            launch = (71.2, s[1])
            if name == "CM5_USB3_TX_N":
                # Escape below the CM5 PCIe fanout, then rise on B.Cu left
                # of the existing long PCIe trunk.
                first, second = ((72.0, 108.0), (103.0, 107.0))
                segment(board, net, s, launch, pcbnew.F_Cu)
                segment(board, net, launch, first, pcbnew.F_Cu)
                transition(board, net, first)
                segment(board, net, first, (82.0, 108.0), pcbnew.B_Cu)
                segment(board, net, (82.0, 108.0), (102.0, 108.0), pcbnew.B_Cu)
                segment(board, net, (102.0, 108.0), second, pcbnew.B_Cu)
                transition(board, net, second)
                segment(board, net, second, d, pcbnew.F_Cu)
                continue
            # TXP takes the lower B.Cu corridor.  Its launch dogbone is
            # intentionally left of TXN's x=72 transition column.
            first = (71.0, 109.0)
            second = (82.0, 112.0)
            segment(board, net, s, launch, pcbnew.F_Cu)
            segment(board, net, launch, first, pcbnew.F_Cu)
            transition(board, net, first)
            segment(board, net, first, second, pcbnew.B_Cu)
            transition(board, net, second)
            segment(board, net, second, d, pcbnew.F_Cu)
            continue
        first, second = via_columns[name]
        s = (pcbnew.ToMM(source.GetPosition().x), pcbnew.ToMM(source.GetPosition().y))
        d = (pcbnew.ToMM(destination.GetPosition().x), pcbnew.ToMM(destination.GetPosition().y))
        # Leave the J7 pad field orthogonally before changing the lane's
        # vertical coordinate; diagonal escapes can clip the neighboring
        # connector ground pads.
        launch = (71.2, s[1])
        segment(board, net, s, launch, pcbnew.F_Cu)
        segment(board, net, launch, (71.2, first[1]), pcbnew.F_Cu)
        segment(board, net, (71.2, first[1]), first, pcbnew.F_Cu)
        transition(board, net, first)
        if name == "CM5_USB3_TX_N":
            # Stay above the existing PCIe B.Cu trunk at y=106 mm.
            segment(board, net, first, (80.0, first[1]), pcbnew.B_Cu)
            segment(board, net, (80.0, first[1]), (102.0, first[1]), pcbnew.B_Cu)
            segment(board, net, (102.0, first[1]), (102.0, second[1]), pcbnew.B_Cu)
            segment(board, net, (102.0, second[1]), second, pcbnew.B_Cu)
        elif name == "CM5_USB3_TX_P":
            # The lower lane goes below the same trunk before crossing its
            # right-hand end; this keeps the B.Cu corridor non-crossing.
            segment(board, net, first, (80.0, 108.5), pcbnew.B_Cu)
            segment(board, net, (80.0, 108.5), (102.0, 108.5), pcbnew.B_Cu)
            segment(board, net, (102.0, 108.5), (102.0, second[1]), pcbnew.B_Cu)
            segment(board, net, (102.0, second[1]), second, pcbnew.B_Cu)
        else:
            segment(board, net, first, second, pcbnew.B_Cu)
        transition(board, net, second)
        segment(board, net, second, d, pcbnew.F_Cu)

    board.BuildListOfNets()
    board.Save(str(OUT))
    print(OUT)


if __name__ == "__main__":
    main()
