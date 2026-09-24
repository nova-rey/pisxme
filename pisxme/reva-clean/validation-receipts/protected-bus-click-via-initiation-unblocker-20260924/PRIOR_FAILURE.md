# Protected-bus via-overlap route-initiation failure

- Clean-base Heavy v2 split attempt at 2.75 GiB; `OOMKilled=false`.
- First J5.2-to-via transaction completed; via-only selection filter was enabled.
- Via properties explicitly showed net `PWR_SRC_J5_P2`, position `(24.514048,24.273596)`.
- After cancelling properties and pressing `x`, KiCad nevertheless entered `Routing Track: 12V_IN_A` at 2.0 mm from overlapping existing copper. The second segment was not authored and no save/candidate/validation occurred.
- Evidence: `idle-after-esc.png`, `via-only-filter.png`, `via-properties-confirm.png`, `second-route-verified-net.png`.
- No canonical CAD changed. Container stopped.
- Classification: GUI route-initiation ambiguity at overlapping via/copper; not a geometry or resource result.
- Next action: authority/Unblocker must select a materially different native initiation method or determine a safe local geometry/control adjustment; do not repeat direct `x` at the overlap.
