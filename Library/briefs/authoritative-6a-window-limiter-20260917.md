# P24-AUTHORITATIVE-6A-LIMITER-EVIDENCE — bounded evidence brief

**Requesting package:** `P24-AUTHORITATIVE-6A-LIMITER-EVIDENCE`  
**Owner:** Librarian  
**Retrieved:** 2026-09-17  
**Disposition:** `CANDIDATE_READY`; the evidence is sufficient for Product/Power Authority reassessment, but no production limiter MPN is qualified by this packet.

## Engineering question

HPQ4 requires six independent 12-V input loops. Each loop must guarantee a full-tolerance and temperature current window of **6.000–6.400 A**, allocate no more than **57 mΩ hot limiter resistance**, and document fault timing, thermal behavior, reverse behavior, and manufacturer provenance. The current MAX17527A and TPS1663 candidates do not satisfy that window. This search looked for an exact limiter MPN and for a controller-plus-external-limiter design with a manufacturer-supported precision contract.

A 6.000–6.400 A window permits a symmetric total current-setting error of at most:

`(1+e)/(1-e) <= 6.400/6.000`, therefore `e <= 3.225806%`.

That budget includes controller threshold, sense element, temperature, calibration residual, and any other guaranteed error. The hot resistance budget is separate and must include the complete current path; a controller data sheet alone does not close it.

## Private Library result

The existing corpus was searched at source, index, brief, subsystem, and protection-dossier levels. It contains the MAX17527A, TPS1663, MAX17526A, external-FET, fuse, TVS, harness, and power-envelope records, but no exact production MPN with a guaranteed 6.000–6.400 A full-tolerance/temperature window and no signed controller-plus-limiter qualification. Existing MAX17527A evidence remains valid within its scope; it is not silently promoted.

The new records below contain manufacturer metadata and extracted facts only. Vendor PDFs were not copied into the private Library and no restricted material was retained. The URLs and revision/date fields are the reproducibility references. No local PDF hash is claimed.

## Manufacturer evidence and disposition

| Source | Exact part/family | Evidence | HPQ4 disposition |
|---|---|---|---|
| [`LTC4281` data sheet](https://www.analog.com/media/en/technical-documentation/data-sheets/ltc4281.pdf), [product page](https://www.analog.com/en/products/ltc4281.html) | `LTC4281AUFD#PBF` / `LTC4281IUFD#PBF` family | ADI 2.9–33 V hot-swap controller, external N-channel FET, nominal 12 V gate drive, I2C programmable current limit, foldback, timer, and fault telemetry. Rev C table gives 32.88–35.87 mV full-scale current-sense threshold and 10–13.5 V gate-drive limits; the 100 mV overcurrent-to-gate-low response is 0.5 µs typ/1 µs max under the stated test condition. | **Candidate architecture only.** The published threshold range is about 4.35% end-to-end before shunt and temperature terms, beyond the 3.2258% total budget. Calibration/trim and production qualification would be required; the data sheet does not itself guarantee the required window or <=57 mΩ hot limiter path. |
| [`LTC4282` data sheet](https://www.analog.com/media/en/technical-documentation/data-sheets/LTC4282.pdf), [product page](https://www.analog.com/en/products/ltc4282.html) | `LTC4282` dual-channel family | ADI 2.9–33 V controller with two external N-channel FET gate circuits, nominal 12 V gate drive, programmable current limit, foldback, timer, and a documented 100 A/12 V application class. | **Candidate architecture only.** Dual-channel packaging is relevant to loop density, but no current-table evidence in this packet proves the complete 6.000–6.400 A window. Authority must qualify threshold, shunt, FET hot RDS(on), calibration, fault, and reverse behavior as a system. |
| [`LM5066H` data sheet](https://www.ti.com/lit/ds/symlink/lm5066h.pdf) | `LM5066H` family | TI 5.5–90 V external-FET hot-swap controller with PMBus, current/power/SOA monitoring, programmable thresholds and fault timing. Full-temperature current-sense limits include 9.2–11.4 mV at the 10 mV setting and 46–54 mV at the 50 mV setting. | **Rejected for this contract.** The threshold tolerance alone is far wider than the 3.2258% total window. It remains useful protection/telemetry precedent only. |
| [`LTC4218` data sheet](https://www.analog.com/media/en/technical-documentation/data-sheets/4218fa.pdf), [product page](https://www.analog.com/en/products/ltc4218.html) | `LTC4218` family | ADI external-FET hot-swap controller, 2.9–26.5 V, 12 V/6 A application example, programmable current limit, timer and foldback. | **Rejected for exact window.** The published current-limit accuracy is 5%, before sense and temperature terms. |
| [`LTC4286` product record](https://www.analog.com/en/products/ltc4286.html) | `LTC4286AUK#PBF` family | ADI high-power 8.5–80 V external-FET hot-swap controller with current limit and monitoring. | **Rejected for exact window.** Published current-limit accuracy is 5%; no complete hot limiter qualification. |
| [`MAX5977A` product record](https://www.analog.com/en/products/max5977a.html) | `MAX5977A` | ADI 1–16 V high-side current-sense/amplifier and external N-channel gate-drive building block; approximately 1% current-sense accuracy is advertised. | **Building block only.** The product record does not establish a closed 6 A active current-limit threshold, fault timing, or complete limiter resistance. It cannot be promoted as an exact limiter MPN. |
| [`TPS24750` product record](https://www.ti.com/product/TPS24750) | `TPS24750RUVR` | TI 2.5–18 V, 12 A eFuse/external blocking-FET controller class; useful 12 V candidate family. | **Unresolved, not promoted.** The current packet does not retain a verified full-temperature current-limit table proving 6.000–6.400 A, nor the complete hot resistance/fault/reverse contract. |

## Existing candidates retained as negative controls

- **MAX17527A:** existing ADI record specifies 0.6–6.0 A and ±4% from 3–6 A across temperature. At the 6.25 kΩ setting the recorded full-tolerance result is 5.7542457542–6.2462462462 A, below the 6.000 A floor. The external FET gate-drive and fault-energy gaps remain as previously recorded.
- **TPS1663:** existing TI record gives ±7% current-limit accuracy. A 6 A setting spans 5.58–6.42 A, below the floor and above the ceiling.
- **MAX17526A:** its ±8.5% full-temperature limit is wider still.

## Candidate architecture boundary

`LTC4281` or `LTC4282` plus a Kelvin precision shunt, a low-hot-resistance external N-channel FET assembly, controlled calibration/trim, and independent production qualification is the closest evidence-backed architecture found. This is an engineering candidate for Product/Power Authority; Librarian does not select it. The authority packet must establish, with manufacturer limits and explicit calculations:

1. source and setpoint range at the actual 12 V input;
2. controller threshold across temperature, supply, and process;
3. shunt tolerance and self-heating;
4. calibrated residual and calibration test method;
5. external FET RDS(on) at the actual gate-drive minimum and hot junction;
6. limiter plus shunt and copper resistance against the 57 mΩ hot allocation;
7. overcurrent, short-circuit, timer, retry/latch, reverse-current and reverse-polarity behavior;
8. SOA, fuse/TVS, connector, harness, and PCB copper coordination for six independent loops.

The current LTC4281 Rev C threshold endpoints alone do not close the window: `35.87/32.88 - 1` is approximately 9.09% end-to-end, or about ±4.35% around the midpoint. Even the zero-scale endpoint ratio `12.9/12.1` is approximately 6.61% end-to-end. Calibration may change the authority result only if the manufacturer contract and production process bound the residual after calibration; it must not be assumed from nominal accuracy language.

## Reassessment recommendation

Return this packet to Product/Power Authority as a **knowledge-complete candidate set with no qualified production MPN**. Keep the package dependency open as `authority:6A-limiter-qualification`, rather than declaring an external blocker. The authority should either:

- qualify a calibrated `LTC4281`/`LTC4282` plus external-limiter assembly with a signed six-loop calculation and production test plan; or
- request one further bounded Researcher search for a manufacturer part whose guaranteed full-temperature current-limit range is already within 6.000–6.400 A.

No CAD, architecture selection, queue state, or product requirement was changed by Librarian.
