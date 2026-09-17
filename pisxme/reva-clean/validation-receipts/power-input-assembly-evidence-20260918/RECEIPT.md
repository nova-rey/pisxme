# High-current input assembly evidence receipt

Librarian indexed and committed the manufacturer evidence packet in private Library commit `82c760b4` on branch `Library`:

- `Library/briefs/high-current-gpu-input-assembly-20260917.md`
- `Library/indexes/high-current-gpu-input-assembly-20260917.json`
- `Library/provenance/high-current-gpu-input-assembly-20260917.json`

The strongest current candidate is Samtec PowerStrip/40: terminal `PET-08-02-T-VT-LC`, mating socket `PES-08-02-T-VT`, and `PESS` 10-AWG cable family (example `PESS-08-10-L-40.00-SR`). The indexed manufacturer test report supports 48.5 A/contact after a 20% derating at 30 C rise with two powered contacts. The immediate supported arrangement is one positive and one return contact; four-contact parallel use has no current-sharing credit without a new authority calculation.

Anderson Powerpole PP15/45 `ASMPR45-1X2-RK` remains a viable fallback with published 40 A CSA/TUV and 45 A UL screening. Amphenol FCI M-CRPS `10170331-360001` remains a secondary candidate requiring exact mating and thermal confirmation.

The existing Molex `0039300020` J5/J6 pair is historical evidence and cannot receive the 40 A continuous / 45 A peak source credit as one positive/return pair. This packet is evidence only: Power/Package Authority must bind one assembly, wire/crimp, installation derating, protection coordination, and complete source-to-J1 resistance/thermal budget before CAD.

No vendor bytes or restricted CAD were copied into the public repository. No CAD was changed. No fabricated-hardware or production-qualification claim is made.
