# ADM1175 component-path evidence brief

- Requesting package: `P24-ADM1175-COMPONENT-PATH-QUALIFICATION`
- Retrieved: 2026-09-17
- Review status: `RESIDUAL_GAP`; no production MPN selected
- Public companion receipt: `validation-receipts/adm1175-component-path-qualification-20260917/`

## Sources

Primary manufacturer sources were consulted directly and only metadata,
revision, URLs and extracted limits are retained here; no vendor PDF bytes are
copied into the public repository.

| Source | Revision / facts retained |
|---|---|
| Analog Devices [ADM1175 Rev. C](https://www.analog.com/media/en/technical-documentation/data-sheets/ADM1175.pdf) | 3.15--16.5 V, 97--103 mV current-limit threshold, gate-drive table at 3.15/5/16.5 V, fast trip/timer equations, Kelvin guidance, 10-lead MSOP ordering options |
| Vishay [WSK2512](https://www.vishay.com/docs/30108/wsk2512.pdf), Rev. 11-Dec-2023 | 4-terminal, 1 W P70, 0.01--0.2 Ω at ±0.1%, ±35 ppm/°C, −65--+170 °C; global numbering yields candidate `WSK2512R0160BEA` |
| Vishay [WSK1206 high power](https://www.vishay.com/docs/30325/wsk120618.pdf), Rev. 15-Dec-2023 | 4-terminal, 0.5 W, 0.01--0.05 Ω at ±0.1%, ±35 ppm/°C; 16 mΩ candidate fails continuous shunt power screen |
| Ohmite [CS10](https://www.ohmite.com/res-cs10/) | 4-terminal Kelvin, 10 W, 1--500 mΩ, ±0.1% available, ±5--100 ppm/°C; no exact 16.13 mΩ standard order code retained |
| Infineon [IRLS4030-7P data sheet](https://www.infineon.com/assets/row/public/documents/24/49/infineon-irls4030-7p-datasheet-en.pdf) | 100 V, D2PAK 7, 4.1 mΩ max at 4.5 V / 94 A / 25 °C, 175 °C, 0.40 °C/W, SOA and avalanche characterization |
| Infineon [BSC070N10LS5](https://www.infineon.com/part/BSC070N10LS5) | Active/preferred, 100 V, SuperSO8 5×6, 8.5 mΩ max at 4.5 V, 79 A, 150 °C |
| Infineon [BSC096N10LS5](https://www.infineon.com/part/BSC096N10LS5) | Active, 100 V, SuperSO8 5×6, 12.5 mΩ max at 4.5 V, 40 A, 175 °C |

## Conclusion

With the exact WSK2512 candidate, the combined ±0.3275% resistance envelope
and ADM1175's 97--103 mV threshold produce 6.042710--6.458652 A. The required
resistance ratio is 1.0045307443 maximum; the candidate is 1.0065715217. No
nominal-value change can repair that ratio without calibration or a tighter
controller threshold. All FET values are 25 °C / 4.5 V screens, not hot
installed guarantees. Gate minimum at PiSXMe's 12.05--12.60 V source, reverse
blocking, fault energy, installed thermal path, and production test residuals
remain authority gates.

This packet is evidence-complete for a precise authority dependency and does
not qualify an ADM1175 production assembly.
