"""Promote the storage selector's actual USB2 source labels to global nets."""
from pathlib import Path
P = Path(__file__).resolve().parent / "STORAGE.kicad_sch"
def main():
    s = P.read_text()
    for name, xy in (("CM5_STORAGE_USB2_DM", "120 183.415"),
                     ("CM5_STORAGE_USB2_DP", "120 182.145")):
        old = f'(label "{name}" (at {xy}'
        new = f'(global_label "{name}" (shape bidirectional) (at {xy}'
        if old not in s: raise SystemExit("missing actual storage label " + name)
        s = s.replace(old, new, 1)
    P.write_text(s)
    print("storage USB2 labels promoted to global")
if __name__ == '__main__': main()
