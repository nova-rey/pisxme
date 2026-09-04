"""Regression gate for the disposable CM5IO-derived Ethernet support island."""
from pathlib import Path
import os
import re
import pcbnew

BOARD = Path(os.environ.get("PISXME_BOARD", Path(__file__).resolve().parents[2] / "pisxme" / "reva-clean" / "CM5IO_DIRECT_J7_ETHERNET_FIXTURE.kicad_pcb"))
REPORT = Path(os.environ.get("PISXME_DRC", str(BOARD.with_name(BOARD.stem + "-edac-rc-reorder2-drc.rpt"))))
REQUIRED = {"ETH_CT1", "ETH_CT2", "ETH_CT3", "ETH_CT4", "ETH_CT_COMMON", "GBE_SHIELD"}


def main():
    board = pcbnew.LoadBoard(str(BOARD))
    names = {n for n in (p.GetNetname().removeprefix("/") for p in board.GetNetsByName().values()) if n}
    missing = REQUIRED - names
    assert not missing, f"missing fixture nets: {sorted(missing)}"
    # Guard the generic KiCad overlay authoring path against the KiCad 10
    # SWIG copy-constructor failure that can serialize zero-length tracks.
    real_signal_tracks = 0
    for item in board.GetTracks():
        if item.GetNetname().removeprefix("/").split("/")[-1].startswith("CM5_GBE_TD"):
            if isinstance(item, pcbnew.PCB_VIA):
                continue
            assert item.GetStart() != item.GetEnd(), "zero-length Ethernet track"
            real_signal_tracks += 1
    assert real_signal_tracks >= 8, "fixture lacks real MDI track geometry"
    report = REPORT.read_text(encoding="utf-8")
    for category in ("tracks_crossing", "shorting_items", "unconnected_items"):
        assert f"[{category}]" not in report, f"electrical DRC category remains: {category}"
    m = re.search(r"\*\* Found (\d+) unconnected pads", report)
    assert m and m.group(1) == "0", "fixture has unconnected pads"
    print("phase17 Ethernet fixture regression: PASS; CT branches and shield electrically closed")


if __name__ == "__main__":
    main()
