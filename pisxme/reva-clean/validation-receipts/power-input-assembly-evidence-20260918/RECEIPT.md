# High-current input assembly evidence receipt

Librarian indexed the manufacturer evidence packet at private Library commit/state `high-current-gpu-input-assembly-20260917`:

- `Library/briefs/high-current-gpu-input-assembly-20260917.md`
- `Library/indexes/high-current-gpu-input-assembly-20260917.json`
- `Library/provenance/high-current-gpu-input-assembly-20260917.json`

Candidate A is Anderson Powerpole PP15/45 assembly `ASMPR45-1X2-RK` with 45 A PCB contacts and 10-AWG-compatible conductors. The packet records manufacturer 40 A CSA/TUV continuous screening and 45 A UL screening, contact resistance calculations, and the limitations of applying those figures to PiSXMe. Candidate B is Amphenol FCI M-CRPS `10170331-360001`, retained as a secondary candidate requiring exact mating and thermal confirmation.

The existing Molex `0039300020` J5/J6 pair is historical evidence and cannot receive the 40 A continuous / 45 A peak source credit as one positive/return pair. This packet is evidence only: Power/Package Authority must bind one assembly, wire/crimp, installation derating, protection coordination, and complete source-to-J1 resistance/thermal budget before CAD.

No vendor bytes or restricted CAD were copied into the public repository. No CAD was changed. No fabricated-hardware or production-qualification claim is made.
