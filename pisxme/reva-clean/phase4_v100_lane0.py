"""Add the schematic-only Rev-A V100 lane-0 island to its child sheet."""

from pathlib import Path
from uuid import UUID

from phase3_scaffold import balanced, make_uuid

ROOT = Path(__file__).resolve().parent
CHILD = ROOT / "V100_PCIE.kicad_sch"
LIBRARY = ROOT / "PiSXMe_RevA_Clean.kicad_sym"
LEGACY_LIBRARY = ROOT.parent / "PiSXMe.kicad_sym"
SXM = 'PiSXMeRevAClean:SXM2_74221_101LF'


def definition(text: str, name: str) -> str:
    start = text.index(f'(symbol "{name}"')
    return balanced(text, start)


def sxm_definition() -> str:
    pins = (
        ('A2', 'PER0_P', -10.16), ('A3', 'PER0_N', -7.62),
        ('E7', 'REFCLK_P', -5.08), ('F7', 'REFCLK_N', -2.54),
        ('E18', 'PERST_N', 0), ('G1', 'PET0_P', 2.54),
        ('G2', 'PET0_N', 5.08), ('PWR', 'VPROT_12V', 7.62),
        ('GND', 'GND', 10.16),
    )
    pin_text = ''.join(
        f'        (pin passive line (at 20.32 {y} 180) (length 5.08)\n'
        f'          (name "{name}" (effects (font (size 1 1))))\n'
        f'          (number "{number}" (effects (font (size 1 1)))))\n'
        for number, name, y in pins
    )
    return f'''(symbol "PiSXMeRevAClean:SXM2_74221_101LF"
      (pin_names (offset 0.8)) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "J" (at 0 -15 0) (effects (font (size 1.27 1.27))))
      (property "Value" "74221-101LF" (at 0 15 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "PiSXMeRevAClean:PiSXMeRevAClean_SXM2_74221_101LF" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
      (property "Datasheet" "https://cdn.amphenol-cs.com/media/wysiwyg/files/drawing/74221.pdf" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
      (symbol "SXM2_74221_101LF_1_1"
        (rectangle (start -15.24 -13) (end 15.24 13) (stroke (width 0.254) (type default)) (fill (type background)))
{pin_text}      )
      (embedded_fonts no)
    )'''


def cap_definition() -> str:
    return '''(symbol "PiSXMeRevAClean:PCIe_AC_COUPLING_C"
      (pin_names (offset 0.8)) (exclude_from_sim no) (in_bom yes) (on_board yes)
      (property "Reference" "C" (at 0 -8 0) (effects (font (size 1.27 1.27))))
      (property "Value" "220nF" (at 0 8 0) (effects (font (size 1.27 1.27))))
      (property "Footprint" "Capacitor_SMD:C_0805_2012Metric" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
      (property "Datasheet" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))
      (symbol "PCIe_AC_COUPLING_C_1_1"
        (rectangle (start -10 -3) (end 10 3) (stroke (width 0.254) (type default)) (fill (type background)))
        (pin passive line (at -15 0 0) (length 5) (name "1" (effects (font (size 1 1)))) (number "1" (effects (font (size 1 1)))))
        (pin passive line (at 15 0 180) (length 5) (name "2" (effects (font (size 1 1)))) (number "2" (effects (font (size 1 1)))))
      )
      (embedded_fonts no)
    )'''


def instance(lib_id: str, ref: str, value: str, x: float, y: float, pins: tuple[str, ...], uid: int, footprint: str = "") -> str:
    pin_lines = ''.join(
        # Pin UUIDs must be distinct from the symbol instance UUID. KiCad's
        # resolver uses these identities when exporting hierarchical nets.
        f'    (pin "{pin}" (uuid {make_uuid(uid + 0x100 + i)}))\n'
        for i, pin in enumerate(pins)
    )
    return f'''  (symbol
    (lib_id "{lib_id}")
    (at {x} {y} 0)
    (unit 1)
    (exclude_from_sim no)
    (in_bom yes)
    (on_board yes)
    (dnp no)
    (uuid {make_uuid(uid)})
    (property "Reference" "{ref}" (at {x} {y - 15} 0) (effects (font (size 1.27 1.27))))
    (property "Value" "{value}" (at {x} {y + 15} 0) (effects (font (size 1.27 1.27))))
    (property "Footprint" "{footprint}" (at {x} {y} 0) (effects (font (size 1.27 1.27)) (hide yes)))
    (property "Datasheet" "https://cdn.amphenol-cs.com/media/wysiwyg/files/drawing/74221.pdf" (at {x} {y} 0) (effects (font (size 1.27 1.27)) (hide yes)))
{pin_lines}    (instances (project "PiSXMe_RevA_Clean" (path "/30000000-0000-0000-0000-000000000000/10000000-0000-0000-0000-000000000002" (reference "{ref}") (unit 1))))
  )\n'''


def main() -> None:
    text = CHILD.read_text()
    if '(lib_id "PiSXMeRevAClean:SXM2_74221_101LF")' in text:
        print('V100 lane-0 island already present')
        return
    sxm = sxm_definition()
    # Reuse only the selected local symbol definition; all four differential
    # paths are explicitly labeled at the connector pins below.
    lib_start = text.index('(lib_symbols')
    lib_end = lib_start + len(balanced(text, lib_start)) - 1
    text = text[:lib_end].rstrip() + '\n' + sxm + '\n' + cap_definition() + text[lib_end:]
    labels = {
        # Direct receive/refclk/reset paths use the CM5-side canonical net
        # names; the corresponding V100 sheet ports remain interface
        # metadata, while PET0 remains explicitly split across C1/C2.
        'A2': 'CM5_PER0_P', 'A3': 'CM5_PER0_N',
        'G1': 'V100_PET0_P', 'G2': 'V100_PET0_N',
        'E7': 'CM5_REFCLK_P', 'F7': 'CM5_REFCLK_N',
        'E18': 'CM5_PERST', 'PWR': 'V100_POWER_12V', 'GND': 'V100_GND',
    }
    ys = {'A2': 89.84, 'A3': 92.38, 'E7': 94.92, 'F7': 97.46,
          'E18': 100.0, 'G1': 102.54, 'G2': 105.08, 'PWR': 107.62, 'GND': 110.16}
    label_text = ''.join(
        f'  (label "{net}" (at 100.32 {ys[pin]} 0) (effects (font (size 1.27 1.27)) (justify left)) '
        f'(uuid {make_uuid(0xc0000000000000000000000000000000 + i)}))\n'
        for i, (pin, net) in enumerate(labels.items())
    )
    body = instance(SXM, 'J_V100', 'Amphenol 74221-101LF Rev-W', 80, 100,
                    tuple(labels), 0xd0000000000000000000000000000000,
                    'PiSXMeRevAClean:PiSXMeRevAClean_SXM2_74221_101LF')
    caps = ''.join(
        instance('PiSXMeRevAClean:PCIe_AC_COUPLING_C', ref, '220nF X7R 50V', 35, y,
                 ('1', '2'), uid, 'Capacitor_SMD:C_0805_2012Metric')
        for ref, y, uid in (
            ('C_PET0_P', 125, 0xd1000000000000000000000000000000),
            ('C_PET0_N', 135, 0xd2000000000000000000000000000000),
        )
    )
    cap_labels = ''.join(
        f'  (label "{net}" (at {x} {y} 0) (effects (font (size 1.27 1.27)) (justify left)) '
        f'(uuid {make_uuid(0xe0000000000000000000000000000000 + i)}))\n'
        for i, (net, x, y) in enumerate((
            ('CM5_PET0_P', 20, 125), ('V100_PET0_P', 50, 125),
            ('CM5_PET0_N', 20, 135), ('V100_PET0_N', 50, 135),
        ))
    )
    marker = '  (sheet_instances '
    text = text.replace(marker, label_text + cap_labels + caps + body + marker, 1)
    CHILD.write_text(text)
    print('V100 lane-0 connector island added; PET0 remains transmitter-side coupling boundary')


if __name__ == '__main__':
    main()
