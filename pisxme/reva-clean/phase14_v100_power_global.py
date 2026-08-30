"""Connect the V100 SXM2 power entry to the protected 12 V rail."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def main() -> None:
    v100 = ROOT / 'V100_PCIE.kicad_sch'
    text = v100.read_text()
    old = '(label "V100_POWER_12V" (at 100.32 107.62 0)'
    new = '(global_label "12V_PROTECTED" (shape bidirectional) (at 100.32 107.62 0)'
    if old in text:
        text = text.replace(old, new, 1)
    elif '(global_label "12V_PROTECTED"' not in text:
        raise SystemExit('V100 power label not found')
    v100.write_text(text)

    power = ROOT / 'POWER_INPUT.kicad_sch'
    text = power.read_text()
    marker = '  (sheet_instances '
    label = '''(global_label "12V_PROTECTED"
  (shape bidirectional)
  (at 70 93.5 0)
  (effects (font (size 1.1 1.1)) (justify left))
  (uuid 0xeb000000-0000-0000-0000-000000000001))
'''
    if '(global_label "12V_PROTECTED"' in text:
        text = text.replace('(at 170 100 0)', '(at 70 93.5 0)', 1)
    else:
        text = text.replace(marker, label + marker, 1)
    power.write_text(text)
    print('V100 SXM2 power entry globally tied to 12V_PROTECTED')

if __name__ == '__main__':
    main()
