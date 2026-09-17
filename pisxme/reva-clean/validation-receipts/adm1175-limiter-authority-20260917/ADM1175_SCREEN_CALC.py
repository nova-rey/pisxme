#!/usr/bin/env python3
"""Deterministic ADM1175 screening calculation; not a production qualification."""
from decimal import Decimal, getcontext
import json
getcontext().prec = 40

R_NOM_OHM = Decimal("0.01613")
R_TOLERANCE = Decimal("0.001")
TEMP_CO_PPM = Decimal("10")
MAX_TEMP_SPAN_C = Decimal("65")
VLIM_MIN_V = Decimal("0.097")
VLIM_MAX_V = Decimal("0.103")
HOT_LIMIT_OHM = Decimal("0.057")
variation = R_TOLERANCE + TEMP_CO_PPM * MAX_TEMP_SPAN_C / Decimal("1000000")
r_min = R_NOM_OHM * (Decimal("1") - variation)
r_max = R_NOM_OHM * (Decimal("1") + variation)
i_min = VLIM_MIN_V / r_max
i_max = VLIM_MAX_V / r_min
p_shunt_max = i_max * i_max * r_min
remaining_hot = HOT_LIMIT_OHM - r_max
result = {
    "screening_only": True,
    "inputs": {
        "rsense_nominal_ohm": str(R_NOM_OHM),
        "initial_tolerance_fraction": str(R_TOLERANCE),
        "tempco_ppm_per_c": str(TEMP_CO_PPM),
        "maximum_temperature_span_c": str(MAX_TEMP_SPAN_C),
        "adm1175_vlim_min_v": str(VLIM_MIN_V),
        "adm1175_vlim_max_v": str(VLIM_MAX_V),
        "hot_limiter_allocation_ohm": str(HOT_LIMIT_OHM),
    },
    "derived": {
        "combined_rsense_variation_fraction": str(variation),
        "rsense_min_ohm": str(r_min),
        "rsense_max_ohm": str(r_max),
        "ilim_min_a": str(i_min),
        "ilim_max_a": str(i_max),
        "shunt_power_at_imax_w": str(p_shunt_max),
        "remaining_hot_allocation_after_max_rsense_ohm": str(remaining_hot),
        "current_floor_margin_a": str(i_min - Decimal("6.000")),
        "current_ceiling_margin_a": str(Decimal("6.400") - i_max),
    },
    "equations": {
        "ilim_min": "0.097 V / R_SENSE_MAX",
        "ilim_max": "0.103 V / R_SENSE_MIN",
        "shunt_power": "I_LIMIT_MAX^2 * R_SENSE_MIN",
        "remaining_hot_allocation": "0.057 ohm - R_SENSE_MAX",
    },
}
print(json.dumps(result, indent=2, sort_keys=True))
