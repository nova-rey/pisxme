#!/usr/bin/env python3
"""Fail-closed contract checks for the retained PiSXMe limiter authority decision.
This is arithmetic/reconciliation evidence, not a hardware qualification.
"""
import json
from pathlib import Path

current_min, current_max = 6.0, 6.4
max_min = current_min * 0.96 / 1.001
max_max = current_min * 1.04 / 0.999
tps_min, tps_max = current_min * .93, current_min * 1.07
ltc_min, ltc_max = 32.88, 35.87
adm_min, adm_max = 6.0427101243, 6.4586520856
allowed_ratio = current_max/current_min
checks = {
  "MAX17527A_floor_fails": max_min < current_min,
  "TPS1663_window_fails": tps_min < current_min and tps_max > current_max,
  "LTC4281_4282_threshold_ratio_exceeds_window": ltc_max/ltc_min > allowed_ratio,
  "ADM1175_WSK2512_window_fails": adm_min >= current_min and adm_max > current_max,
  "no_production_selection": True,
}
if not all(checks.values()):
    raise SystemExit(f"FAIL: unexpected contract result: {checks}")
print(json.dumps({
  "status":"PASS_ARITHMETIC_NO_GO",
  "checks":checks,
  "values":{
    "MAX17527A_A":[max_min,max_max],
    "TPS1663_A":[tps_min,tps_max],
    "LTC4281_4282_ratio":ltc_max/ltc_min,
    "allowed_current_ratio":allowed_ratio,
    "ADM1175_WSK2512_A":[adm_min,adm_max],
  },
  "interpretation":"No retained candidate closes the complete HPQ4 limiter-system contract; this does not claim hardware qualification."
}, indent=2))
