#!/usr/bin/env python3
"""Graft V121 USB3 route objects by reading its serialized native PCB records.

The historical fixture's pcbnew track iterator is unavailable in the current
binding, so this helper parses only the four route-net segment/via records from
the saved KiCad syntax, then creates ordinary native PCB objects in the current
M-key candidate. Connectivity is still established and audited by KiCad.
"""
from pathlib import Path
import re
import pcbnew

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "PHASE24_STORAGE_USB3_SHIFTED_ESCAPE_V121.kicad_pcb"
BASE = ROOT / "PHASE24_STORAGE_MKEY_POWER_ACTUAL_PAD_PROBE_20260912.kicad_pcb"
OUTPUT = ROOT / "PHASE24_STORAGE_MKEY_USB3_SERIALIZED_V121_20260912.kicad_pcb"
NETS = {"CM5_USB3_RX_N", "CM5_USB3_RX_P", "CM5_USB3_TX_N", "CM5_USB3_TX_P"}


def vector(x, y):
    return pcbnew.VECTOR2I_MM(float(x), float(y))


def net(board, name):
    value = board.FindNet(name)
    if value is None:
        raise RuntimeError(f"missing target net {name}")
    return value


def records(text):
    for match in re.finditer(r"\n\t\((segment|via)\n(.*?)\n\t\)", text, re.S):
        kind, body = match.groups()
        nm = re.search(r'\(net "([^"]+)"\)', body)
        if not nm or nm.group(1) not in NETS:
            continue
        layer = re.search(r'\(layer "([^"]+)"\)', body)
        width = re.search(r'\(width ([0-9.]+)\)', body)
        if kind == "segment":
            start = re.search(r'\(start ([0-9.]+) ([0-9.]+)\)', body)
            end = re.search(r'\(end ([0-9.]+) ([0-9.]+)\)', body)
            if not start or not end or not layer or not width:
                raise RuntimeError(f"incomplete segment record for {nm.group(1)}")
            yield (kind, nm.group(1), start.groups(), end.groups(),
                   layer.group(1), float(width.group(1)))
        else:
            at = re.search(r'\(at ([0-9.]+) ([0-9.]+)\)', body)
            size = re.search(r'\(size ([0-9.]+)\)', body)
            drill = re.search(r'\(drill ([0-9.]+)\)', body)
            layers = re.search(r'\(layers "([^"]+)" "([^"]+)"\)', body)
            if not at or not size or not drill or not layers:
                raise RuntimeError(f"incomplete via record for {nm.group(1)}")
            yield (kind, nm.group(1), at.groups(), float(size.group(1)),
                   float(drill.group(1)), layers.groups())


def main():
    board = pcbnew.LoadBoard(str(BASE))
    if board is None:
        raise SystemExit("cannot load base board")
    for item in list(board.GetTracks()):
        if item.GetNetname() in NETS:
            board.RemoveNative(item)
    count = 0
    for record in records(SOURCE.read_text()):
        if record[0] == "segment":
            _, name, start, end, layer, width = record
            item = pcbnew.PCB_TRACK(board)
            item.SetStart(vector(*start)); item.SetEnd(vector(*end))
            item.SetLayer(board.GetLayerID(layer)); item.SetWidth(pcbnew.FromMM(width))
        else:
            _, name, at, size, drill, layers = record
            item = pcbnew.PCB_VIA(board)
            item.SetPosition(vector(*at)); item.SetWidth(pcbnew.FromMM(size))
            item.SetDrill(pcbnew.FromMM(drill))
            item.SetLayerPair(board.GetLayerID(layers[0]), board.GetLayerID(layers[1]))
        item.SetNetCode(net(board, name).GetNetCode()); board.Add(item); count += 1
    board.BuildListOfNets(); board.Save(str(OUTPUT)); print(f"grafted {count} records to {OUTPUT}")


if __name__ == "__main__": main()
