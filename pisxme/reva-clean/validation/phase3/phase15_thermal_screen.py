"""Conservative TPSM63606 thermal screen from the Phase 5 design envelope."""

RAILS = {
    "CM5_5V": (5.0, 3.0),
    "BRIDGE_3V3": (3.3, 2.0),
    "BRIDGE_1V1": (1.1, 1.0),
}
EFFICIENCY = 0.90
AMBIENT_C = 50.0
R_THETA_JA = 33.1  # TI SLVSGB4B table 7-4, conservative listed value
TJ_LIMIT_C = 125.0


def main():
    for rail, (voltage, current) in RAILS.items():
        output_w = voltage * current
        loss_w = output_w * (1.0 / EFFICIENCY - 1.0)
        junction_c = AMBIENT_C + loss_w * R_THETA_JA
        margin_c = TJ_LIMIT_C - junction_c
        assert margin_c > 0.0, (rail, junction_c, margin_c)
        print(f"{rail}: P_loss={loss_w:.3f}W, Tj={junction_c:.1f}C, margin={margin_c:.1f}C")
    print("Phase 15 thermal screen: PASS; board-specific thermal proof remains empirical")


if __name__ == "__main__":
    main()
