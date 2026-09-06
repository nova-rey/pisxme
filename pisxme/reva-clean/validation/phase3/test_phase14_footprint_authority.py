from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRETTY = ROOT / "PiSXMe_RevA_Clean.pretty"


def main() -> None:
    expected = {
        "LM74700QDBVRQ1_SOT23_6.kicad_mod": 6,
        "TPSM63606RDLR_RDL0020.kicad_mod": 20,
        "TUSB9261IPVP_PVP0064A.kicad_mod": 65,
        "TPD4E004DRYR_WSON6.kicad_mod": 6,
    }
    for name, count in expected.items():
        text = (PRETTY / name).read_text()
        assert text.count('(pad "') == count, name
    for sheet in ROOT.glob("*.kicad_sch"):
        if sheet.name in {"storage_head_test.kicad_sch", "storage_variant_no_defs.kicad_sch", "storage_variant_no_clock.kicad_sch"}:
            continue
        text = sheet.read_text()
        for mpn, fp in (
            ("LM74700QDBVRQ1", "LM74700QDBVRQ1_SOT23_6"),
            ("TPSM63606RDLR", "TPSM63606RDLR_RDL0020"),
            ("TUSB9261IPVP", "TUSB9261IPVP_PVP0064A"),
            ("TPD4E004DRYR", "TPD4E004DRYR_WSON6"),
        ):
            if f'property "MPN" "{mpn}"' in text:
                assert f'property "Footprint" "PiSXMeRevAClean:{fp}"' in text
    regulator = (PRETTY / "TPSM63606RDLR_RDL0020.kicad_mod").read_text()
    assert '(pad "1" smd roundrect (at -2.250 -2.000 0)' in regulator
    assert '(pad "16" smd roundrect (at 2.250 -2.000 180)' in regulator
    for number, coordinate in ((17, "0 -1.125"), (18, "0 -0.375"),
                               (19, "0 0.375"), (20, "0 1.125")):
        assert f'(pad "{number}" smd roundrect (at {coordinate})' in regulator
    molex = (PRETTY / "Molex_0039300020_5569_2P_RA.kicad_mod").read_text()
    assert '(pad "1" thru_hole rect (at 0 0)' in molex
    assert '(pad "2" thru_hole circle (at 0 5.5)' in molex
    assert '(pad "MP1" np_thru_hole circle (at 0 -7.3)' in molex
    assert 'pad "MP2"' not in molex
    assert 'at 4.2 0' not in molex
    fuse = (PRETTY / "ATO_FuseHolder_17861650001.kicad_mod").read_text()
    for number, coordinate in ((1, "-6.4 -1.25"), (2, "-6.4 1.25"),
                               (3, "-2.9 -1.25"), (4, "-2.9 1.25"),
                               (5, "2.9 -1.25"), (6, "2.9 1.25"),
                               (7, "6.4 -1.25"), (8, "6.4 1.25")):
        assert f'(pad "{number}"' in fuse and f'(at {coordinate})' in fuse
    assert '(pad "MP1" np_thru_hole circle (at 0 0)' in fuse
    assert 'at -7.62 0' not in fuse and 'at -5.08 0' not in fuse
    print("Phase 14 footprint authority: PASS; Littelfuse eight-hole FLR pattern and Molex layout assigned")


if __name__ == "__main__":
    main()
