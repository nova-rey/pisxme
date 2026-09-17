#!/usr/bin/env python3
"""Deterministic replacement calculator for HPQ4's missing calculator.

This file is a newly authored replacement.  It is deliberately not named or
represented as recovery of the missing HPQ4 POWER_BUDGET_CALC.py.  All inputs
are read from the imported, signed POWER_BUDGET_CORRECTION.json; no CAD or
product-envelope values are edited here.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any

getcontext().prec = 50
HERE = Path(__file__).resolve().parent
SOURCE = HERE / "POWER_BUDGET_CORRECTION.json"
EXPECTED_SOURCE_SHA256 = "321e4d14c3696d1d24c9ccb54c17526e339786b527e73b54b1ebd0100c501eae"


def dec(value: Any) -> Decimal:
    """Convert JSON numbers or decimal strings without binary-float arithmetic."""
    return Decimal(str(value))


def fmt(value: Decimal) -> str:
    return format(value, "f")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rounded(value: Decimal, places: int = 9) -> Decimal:
    return value.quantize(Decimal(1).scaleb(-places))


def close(name: str, actual: Decimal, expected: Any, checks: list[dict[str, Any]], places: int = 9) -> None:
    expected_d = dec(expected)
    actual_r = rounded(actual, places)
    expected_r = rounded(expected_d, places)
    difference = abs(actual_r - expected_r)
    allowed = Decimal(1).scaleb(-places)
    passed = difference <= allowed
    checks.append({
        "name": name,
        "actual": fmt(actual_r),
        "expected": fmt(expected_r),
        "difference": fmt(difference),
        "tolerance": fmt(allowed),
        "status": "PASS" if passed else "FAIL",
    })
    if not passed:
        raise AssertionError(f"{name}: {actual_r} != {expected_r} within {allowed}")


def require(condition: bool, message: str) -> None:
    """Fail closed even when Python is invoked with -O."""
    if not condition:
        raise ValueError(message)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="emit the deterministic calculation report as JSON")
    args = parser.parse_args()

    require(SOURCE.is_file(), f"missing signed authority input: {SOURCE}")
    actual_source_sha256 = sha256(SOURCE)
    require(
        actual_source_sha256 == EXPECTED_SOURCE_SHA256,
        f"signed authority input hash mismatch: {actual_source_sha256} != {EXPECTED_SOURCE_SHA256}",
    )
    source = json.loads(SOURCE.read_text())
    checks: list[dict[str, Any]] = []
    decision = source["decision"]
    product = source["product_constraints"]
    load = source["load_accounting"]
    source_contract = source["source_contract"]
    loops = source["independent_loop_contract"]
    ir = source["static_ir_budget"]
    transient = source["transient_pdn_contract"]

    # Pin the authority identity and product invariants before doing arithmetic.
    require(decision["id"] == "PISXME-P24-POWER-BUDGET-HPQ4", "unexpected authority decision id")
    require(decision["version"] == "2.0.0", "unexpected authority decision version")
    require(
        decision["status"] == "SIGNED_NUMERICAL_CONTRACT_DOWNSTREAM_QUALIFICATION_GATED",
        "authority decision is not the signed numerical contract",
    )
    require(product["independent_loop_count"] == 6, "authority contract does not define six independent loops")
    require(product["passive_sharing_credit_allowed"] is False, "passive-sharing credit is not permitted")

    efficiency = dec(product["efficiency_floor"])
    auxiliary = dec(product["auxiliary_functional_load_w"])
    loop_count = dec(product["independent_loop_count"])
    sustained_bus_min = dec(product["protected_bus_min_v"]["sustained"])
    peak_bus_min = dec(product["protected_bus_min_v"]["peak"])
    branch_cap = dec(ir["per_branch_total_resistance_cap_ohm_exact"])
    common_cap = dec(ir["common_bus_positive_and_return_cap_ohm_exact"])
    complete_equivalent = dec(ir["balanced_complete_path_equivalent_ohm_exact"])

    scenarios: dict[str, dict[str, Decimal]] = {}
    for name, key, bus_min in (
        ("sustained", "v100_sustained_w", sustained_bus_min),
        ("peak", "v100_peak_w", peak_bus_min),
    ):
        v100 = dec(product[key])
        bus_power = (v100 + auxiliary) / efficiency
        total_current = bus_power / bus_min
        per_loop = total_current / loop_count
        s = load[name]
        expected_per_loop = s["per_loop_a"]
        close(f"load_accounting.{name}.bus_power_w", bus_power, s["bus_power_w"], checks)
        close(f"load_accounting.{name}.total_current_a", total_current, s["total_current_a"], checks)
        close(f"load_accounting.{name}.per_loop_a", per_loop, expected_per_loop, checks)
        source_cap = dec(source_contract["continuous_current_capability_min_a"] if name == "sustained" else source_contract["bounded_peak_current_capability_min_a"])
        source_margin = source_cap - total_current
        close(f"source_contract.current_margin_a.{name}", source_margin, source_contract["current_margin_a"][name], checks)

        branch_drop = per_loop * branch_cap
        common_drop = total_current * common_cap
        complete_drop = branch_drop + common_drop
        source_min = dec(source_contract["sustained_voltage_at_S0_v"]["min"] if name == "sustained" else source_contract["peak_voltage_at_S0_v"]["min"])
        protected_lower = source_min - complete_drop
        bus_margin = protected_lower - bus_min
        static_expected = ir[name]
        close(f"static_ir_budget.{name}.branch_drop_v", branch_drop, static_expected["branch_drop_v"], checks)
        close(f"static_ir_budget.{name}.common_drop_v", common_drop, static_expected["common_drop_v"], checks)
        close(f"static_ir_budget.{name}.total_drop_v", complete_drop, static_expected["total_drop_v"], checks)
        close(f"static_ir_budget.{name}.protected_bus_lower_bound_v", protected_lower, static_expected["protected_bus_lower_bound_v"], checks)
        close(f"static_ir_budget.{name}.margin_over_minimum_v", bus_margin, static_expected["margin_over_minimum_v"], checks)
        scenarios[name] = {
            "bus_power_w": bus_power,
            "total_current_a": total_current,
            "per_loop_a": per_loop,
            "source_current_margin_a": source_margin,
            "branch_drop_v": branch_drop,
            "common_drop_v": common_drop,
            "total_drop_v": complete_drop,
            "protected_bus_lower_bound_v": protected_lower,
            "margin_over_minimum_v": bus_margin,
        }

    ceiling_branch = dec(loops["full_tolerance_operational_ceiling_a_per_loop"])
    ceiling_total = ceiling_branch * loop_count
    ceiling_branch_drop = ceiling_branch * branch_cap
    ceiling_common_drop = ceiling_total * common_cap
    ceiling_complete = ceiling_branch_drop + ceiling_common_drop
    ceiling = ir["full_derated_ceiling"]
    close("static_ir_budget.full_derated_ceiling.branch_drop_v", ceiling_branch_drop, ceiling["branch_drop_v"], checks)
    close("static_ir_budget.full_derated_ceiling.common_drop_v", ceiling_common_drop, ceiling["common_drop_v"], checks)
    close("static_ir_budget.full_derated_ceiling.complete_drop_v", ceiling_complete, ceiling["complete_drop_v"], checks)
    derived_complete_equivalent = branch_cap + loop_count * common_cap
    close(
        "static_ir_budget.derived_balanced_complete_path_equivalent_ohm",
        derived_complete_equivalent,
        complete_equivalent,
        checks,
        places=12,
    )
    close("static_ir_budget.balanced_complete_path_equivalent_mohm", complete_equivalent * Decimal(1000), ir["balanced_complete_path_equivalent_mohm"], checks, places=6)

    current_step = scenarios["peak"]["total_current_a"] - scenarios["sustained"]["total_current_a"]
    droop_budget = scenarios["peak"]["margin_over_minimum_v"]
    dynamic_impedance = droop_budget / current_step
    close("transient_pdn_contract.current_step_total_a", current_step, transient["current_step_total_a"], checks)
    close("transient_pdn_contract.additional_dynamic_droop_budget_at_peak_v", droop_budget, transient["additional_dynamic_droop_budget_at_peak_v"], checks)
    close("transient_pdn_contract.additional_dynamic_impedance_upper_bound_ohm", dynamic_impedance, transient["additional_dynamic_impedance_upper_bound_ohm"], checks)

    report = {
        "schema_version": 1,
        "artifact_identity": "PISXME-P24-POWER-BUDGET-CALCULATOR-REPLACEMENT",
        "artifact_status": "NEW_REPLACEMENT_NOT_RECOVERED_HPQ_SOURCE",
        "source": {
            "path": SOURCE.name,
            "sha256": actual_source_sha256,
            "decision_id": decision["id"],
            "decision_version": decision["version"],
            "base_sha": decision["base_sha"],
            "historical_missing_path": "POWER_BUDGET_CALC.py",
            "historical_missing_path_recovered": False,
        },
        "method": {
            "arithmetic": "Python Decimal, precision 50",
            "source_to_p0_loss_separate": True,
            "returns_included_in_every_cap": True,
            "passive_sharing_credit": False,
            "branch_drop_equation": "Ibranch*0.148250 + Itotal*0.001333333333333333333333333333",
        },
        "scenarios": {name: {key: fmt(value) for key, value in values.items()} for name, values in scenarios.items()},
        "full_derated_ceiling": {
            "branch_current_a": fmt(ceiling_branch),
            "aggregate_current_a": fmt(ceiling_total),
            "branch_drop_v": fmt(ceiling_branch_drop),
            "common_drop_v": fmt(ceiling_common_drop),
            "complete_drop_v": fmt(ceiling_complete),
        },
        "transient": {
            "current_step_total_a": fmt(current_step),
            "additional_dynamic_droop_budget_at_peak_v": fmt(droop_budget),
            "additional_dynamic_impedance_upper_bound_ohm": fmt(dynamic_impedance),
            "recovery_to_valid_window_max_ms": transient["recovery_to_valid_window_max_ms"],
        },
        "assertions": {"count": len(checks), "status": "PASS", "checks": checks},
        "downstream_gates_preserved": source["downstream_gates"],
        "generated_by": "POWER_BUDGET_CALC_REPLACEMENT.py",
    }
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(f"{report['artifact_identity']}: {report['assertions']['status']} ({len(checks)} assertions)")
        print(f"source={report['source']['sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
