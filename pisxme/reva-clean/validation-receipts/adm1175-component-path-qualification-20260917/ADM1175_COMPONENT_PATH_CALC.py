#!/usr/bin/env python3
"""Fail-closed screening arithmetic for the ADM1175 component-path packet."""
from decimal import Decimal, getcontext
import json

getcontext().prec = 40
VLIM_MIN_V = Decimal("0.097")
VLIM_MAX_V = Decimal("0.103")
I_MIN_A = Decimal("6.000")
I_MAX_A = Decimal("6.400")
HOT_PATH_MAX_MOHM = Decimal("57.0")

# Candidate from the documented Vishay WSK2512 global numbering scheme:
# 16 mOhm, 0.1%, 4-terminal, 1 W P70, component TCR +/-35 ppm/C.
SHUNT_NOM_MOHM = Decimal("16.0")
SHUNT_TOL = Decimal("0.001")
SHUNT_TCR_PPM_C = Decimal("35")
TEMP_DELTA_C = Decimal("65")

variation = SHUNT_TOL + SHUNT_TCR_PPM_C * TEMP_DELTA_C / Decimal("1000000")
r_min_mohm = SHUNT_NOM_MOHM * (Decimal("1") - variation)
r_max_mohm = SHUNT_NOM_MOHM * (Decimal("1") + variation)
r_min_ohm = r_min_mohm / Decimal("1000")
r_max_ohm = r_max_mohm / Decimal("1000")
i_min_a = VLIM_MIN_V / r_max_ohm
i_max_a = VLIM_MAX_V / r_min_ohm
shunt_power_w = i_max_a * i_max_a * r_max_ohm

# This ratio test is independent of nominal resistor value.
required_resistance_ratio = (VLIM_MIN_V / I_MIN_A) / (VLIM_MAX_V / I_MAX_A)
actual_resistance_ratio = r_max_mohm / r_min_mohm
ratio_pass = actual_resistance_ratio <= required_resistance_ratio

fet_screens = [
    {
        "mpn": "IRLS4030-7PPbF",
        "manufacturer": "Infineon Technologies",
        "package": "D2PAK 7-pin / TO-263 7-pin",
        "vds_max_v": 100,
        "rds_on_max_mohm_at_4p5v_25c": Decimal("4.1"),
        "source_current_test_a": Decimal("94"),
        "rtheta_jc_max_c_per_w": Decimal("0.40"),
        "tj_max_c": 175,
        "hot_rds_qualified": False,
    },
    {
        "mpn": "BSC070N10LS5ATMA1",
        "manufacturer": "Infineon Technologies",
        "package": "PG-TDSON-8 / SuperSO8 5x6",
        "vds_max_v": 100,
        "rds_on_max_mohm_at_4p5v_25c": Decimal("8.5"),
        "source_current_test_a": None,
        "rtheta_jc_max_c_per_w": None,
        "tj_max_c": 150,
        "hot_rds_qualified": False,
    },
    {
        "mpn": "BSC096N10LS5ATMA1",
        "manufacturer": "Infineon Technologies",
        "package": "PG-TDSON-8 / SuperSO8 5x6",
        "vds_max_v": 100,
        "rds_on_max_mohm_at_4p5v_25c": Decimal("12.5"),
        "source_current_test_a": None,
        "rtheta_jc_max_c_per_w": None,
        "tj_max_c": 175,
        "hot_rds_qualified": False,
    },
]

for fet in fet_screens:
    fet["residual_57mohm_at_25c_only"] = HOT_PATH_MAX_MOHM - r_max_mohm - fet["rds_on_max_mohm_at_4p5v_25c"]
    fet["residual_is_not_hot_qualification"] = True

out = {
    "schema_version": 1,
    "calculation": "ADM1175 Rev. C Equations 1-3",
    "controller_threshold_v": {"min": str(VLIM_MIN_V), "nominal": "0.100", "max": str(VLIM_MAX_V)},
    "hpq4_window_a": [str(I_MIN_A), str(I_MAX_A)],
    "hot_path_max_mohm": str(HOT_PATH_MAX_MOHM),
    "candidate_shunt": {
        "family": "Vishay WSK2512",
        "derived_mpn": "WSK2512R0160BEA",
        "nominal_mohm": str(SHUNT_NOM_MOHM),
        "initial_tolerance": str(SHUNT_TOL),
        "component_tcr_ppm_c": str(SHUNT_TCR_PPM_C),
        "temperature_span_c": str(TEMP_DELTA_C),
        "combined_resistance_variation": str(variation),
        "r_min_mohm": str(r_min_mohm),
        "r_max_mohm": str(r_max_mohm),
        "power_at_i_max_w": str(shunt_power_w),
    },
    "screen_result": {
        "ilim_min_a": str(i_min_a),
        "ilim_max_a": str(i_max_a),
        "current_window_pass": bool(i_min_a >= I_MIN_A and i_max_a <= I_MAX_A),
        "required_resistance_ratio_max": str(required_resistance_ratio),
        "actual_resistance_ratio": str(actual_resistance_ratio),
        "ratio_pass": bool(ratio_pass),
    },
    "fet_screens": fet_screens,
    "qualification_status": "RESIDUAL_GAP",
    "residual_gates": [
        "ADM1175 GATE minimum at signed 12.05-12.60 V source is not guaranteed by a table value",
        "external FET hot RDS(on) at that minimum gate drive is not manufacturer-guaranteed",
        "reverse blocking/reverse polarity behavior and back-to-back-FET resistance are unbound",
        "harness transient and TVS/fuse/nFET SOA-I2t coordination are unbound",
        "installed copper/Kelvin resistance and thermal installation are unbound",
        "six-loop calibration residual, fixture accuracy, retention, and lot traceability are unbound",
    ],
}

def json_default(value):
    if isinstance(value, Decimal):
        return str(value)
    raise TypeError(type(value).__name__)

print(json.dumps(out, indent=2, default=json_default, sort_keys=True))
