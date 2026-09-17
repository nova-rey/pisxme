# Protected-bus corrective authority

Decision `PISXME-P24-PROTECTED-BUS-CORRECTIVE-20260918` binds the minimum correction after exact validation of candidate `20c9cb12` failed.

## Findings

The exact integrated candidate failed DRC/ERC/connectivity and its segment-only extraction estimated `12V_PROTECTED` at approximately 0.2787 ohm and `POWER_GND` at approximately 0.6314 ohm. These exclude pads, planes, vias, contacts, temperature and spreading, so they cannot close the 10 mOhm complete positive-plus-return contract. The current J5/J6 topology has one 12 V contact and one return per branch; no 40/45 A credit is permitted for that assembly without a changed or fully qualified input assembly.

## Binding correction

Retain the selected protected/distributed 12 V common-bus architecture. Replace or materially rework the source/input assembly and its complete positive-plus-return path so the exact connector, harness/crimp, protection, copper/via/plane, and J1 field are rated and extracted against 300 W sustained and 330 W for 100 ms. Preserve ordinary protection, no unqualified passive-sharing credit, 11.4–12.6 V source window, 11.05/11.00 V protected minima, and 10 mOhm complete path maximum. The producer must return one candidate; it must not revive six precision loops.

The exact source connector/harness MPN, fuse I2t/SOA, protection thresholds, thermal rise, load-step waveform, and standalone SXM2 sequencing remain prototype-validation items where evidence is unavailable. No hardware or production qualification is claimed.
