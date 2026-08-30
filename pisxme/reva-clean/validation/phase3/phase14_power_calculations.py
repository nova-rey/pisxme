#!/usr/bin/env python3
"""Reproducible Rev-A Phase 5 design-envelope calculations."""
from dataclasses import dataclass

@dataclass(frozen=True)
class PowerEnvelope:
    v_in: float = 12.0
    efficiency: float = 0.90
    v100_w: float = 250.0
    cm5_5v_a: float = 3.0
    bridge_3v3_a: float = 2.0
    bridge_1v1_a: float = 1.0
    branch_count: int = 2
    fuse_a: float = 15.0

def calculate(e=PowerEnvelope()):
    v100_a = e.v100_w / (e.v_in * e.efficiency)
    lv_w = 5.0 * e.cm5_5v_a + 3.3 * e.bridge_3v3_a + 1.1 * e.bridge_1v1_a
    lv_a = lv_w / (e.v_in * e.efficiency)
    total_a = v100_a + lv_a
    shared_a = total_a / e.branch_count
    fet_rds = 0.0027  # CSD19536KCS max at 10 V, TI datasheet
    return {
        'v100_input_a': v100_a, 'low_voltage_input_a': lv_a,
        'total_input_a': total_a, 'branch_shared_a': shared_a,
        'shared_branch_margin_a': e.fuse_a - shared_a,
        'single_branch_overload_a': total_a - e.fuse_a,
        'fet_loss_shared_w': shared_a * shared_a * fet_rds,
        'fet_loss_single_branch_w': total_a * total_a * fet_rds,
        'tvs_clamp_margin_v': 42.0 - 29.2,
        'one_point_one_v_nominal': 1.0 * (1.0 + 1.0 / 10.0),
        'one_point_one_v_cout_derated_uf': 16.0 * 22.0 * 0.90,
    }

def main():
    r = calculate()
    assert abs(r['total_input_a'] - 25.25) < 0.01
    assert r['branch_shared_a'] < 15.0 and r['single_branch_overload_a'] > 0
    assert r['fet_loss_shared_w'] < 0.5 and r['tvs_clamp_margin_v'] > 0
    assert abs(r['one_point_one_v_nominal'] - 1.10) < 1e-9
    assert r['one_point_one_v_cout_derated_uf'] >= 300.0
    print('Phase 5 power calculations: PASS (design envelope; residual physical risk recorded)')
    for k, v in r.items(): print(f'  {k}={v:.4f}')

if __name__ == '__main__': main()
