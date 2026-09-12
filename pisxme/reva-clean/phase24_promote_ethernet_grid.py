"""Promote the proven Ethernet support-group grid correction.

This is deliberately exact and fail-closed. It moves only the serialized
coordinates identified by the disposable native probe; no labels, values,
UUIDs, pins, or connectivity records are changed.
"""
from pathlib import Path

PATH = Path(__file__).resolve().parent / "ETHERNET.kicad_sch"

def row(x, nx, *, cy=True):
    pairs = {
        f"(at {x} 50 0)": f"(at {nx} 50.8 0)",
        f"(at {x} 46 0)": f"(at {nx} 46.99 0)",
        f"(at {x} 54 0)": f"(at {nx} 54.8 0)",
        f"(at {x} 46.19 0)": f"(at {nx} 46.99 0)",
        f"(at {x} 53.81 0)": f"(at {nx} 54.61 0)",
        f"(at {x} 60 0)": f"(at {nx} 60.96 0)",
        f"(at {x} 56 0)": f"(at {nx} 57.15 0)",
        f"(at {x} 64 0)": f"(at {nx} 64.96 0)",
        f"(at {x} 56.19 0)": f"(at {nx} 57.15 0)",
        f"(at {x} 63.81 0)": f"(at {nx} 64.77 0)",
    }
    return pairs

def main():
    text = PATH.read_text()
    pairs = {}
    for x, nx in (("108", "107.95"), ("116", "115.57"),
                  ("124", "123.19"), ("132", "130.81"),
                  ("145", "144.78"), ("155", "154.94")):
        pairs.update(row(x, nx))
    pairs.update({
        "(at 108 75 0)": "(at 107.95 74.93 0)",
        "(at 108 71.19 0)": "(at 107.95 71.12 0)",
        "(at 108 79 0)": "(at 107.95 78.93 0)",
        "(at 108 78.81 0)": "(at 107.95 78.74 0)",
    })
    total = 0
    for old, new in pairs.items():
        count = text.count(old)
        if count == 0:
            continue
        text = text.replace(old, new)
        total += count
    if total < 100:
        raise SystemExit(f"refusing partial promotion: only {total} coordinate records")
    PATH.write_text(text)
    print(f"promoted Ethernet grid coordinates: {total} records")

if __name__ == "__main__":
    main()
