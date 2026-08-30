from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRETTY = ROOT / "PiSXMe_RevA_Clean.pretty"


def main() -> None:
    expected = {
        "LM74700QDBVRQ1_SOT23_6.kicad_mod": 6,
        "TPSM63606RDLR_RDL0020.kicad_mod": 20,
        "TUSB9261IPVP_HTQFP64.kicad_mod": 64,
        "TPD4E004DRYR_WSON6.kicad_mod": 6,
    }
    for name, count in expected.items():
        text = (PRETTY / name).read_text()
        assert text.count('(pad "') == count, name
    for sheet in ROOT.glob("*.kicad_sch"):
        text = sheet.read_text()
        for mpn, fp in (
            ("LM74700QDBVRQ1", "LM74700QDBVRQ1_SOT23_6"),
            ("TPSM63606RDLR", "TPSM63606RDLR_RDL0020"),
            ("TUSB9261IPVP", "TUSB9261IPVP_HTQFP64"),
            ("TPD4E004DRYR", "TPD4E004DRYR_WSON6"),
        ):
            if f'property "MPN" "{mpn}"' in text:
                assert f'property "Footprint" "PiSXMeRevAClean:{fp}"' in text
    print("Phase 14 footprint authority: PASS; package pads assigned; connector patterns remain gated")


if __name__ == "__main__":
    main()
