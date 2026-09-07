#!/usr/bin/env python3
"""Set a disposable board's copper minimum to the documented JLC probe value."""
import argparse
import pcbnew

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("output")
    a = ap.parse_args()
    b = pcbnew.LoadBoard(a.input)
    if b is None:
        raise SystemExit("native board load failed")
    d = b.GetDesignSettings()
    d.m_MinClearance = pcbnew.FromMM(0.15)
    b.Save(a.output)
    print(a.output)

if __name__ == "__main__":
    main()
