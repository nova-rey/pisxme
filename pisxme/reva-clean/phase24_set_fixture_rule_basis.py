#!/usr/bin/env python3
"""Author a disposable native KiCad rule basis for the JLC 0.15 mm probe.

This changes only the disposable board's native design settings.  It does not
alter production project rules or suppress DRC findings.
"""
import argparse
import pcbnew


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("output")
    ap.add_argument("--clearance", type=float, default=0.15)
    args = ap.parse_args()

    board = pcbnew.LoadBoard(args.input)
    if board is None:
        raise SystemExit("native board load failed")

    value = pcbnew.FromMM(args.clearance)
    settings = board.GetDesignSettings()
    settings.m_MinClearance = value
    net_settings = settings.m_NetSettings
    default = net_settings.GetDefaultNetclass()
    default.SetClearance(value)
    net_settings.SetDefaultNetclass(default)
    net_settings.RecomputeEffectiveNetclasses()
    board.Save(args.output)
    print(f"saved {args.output}")
    print(f"global_min_clearance_mm={pcbnew.ToMM(settings.m_MinClearance):.4f}")
    print(f"default_netclass_clearance_mm={pcbnew.ToMM(net_settings.GetDefaultNetclass().GetClearance()):.4f}")


if __name__ == "__main__":
    main()
