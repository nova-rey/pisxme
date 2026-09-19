# P24-MECHANICS-L10-U11-LOCAL-CORRECTION

- Base SHA: `c7c8cd885259bcb17a4a76b7ba9809d57cc96b0d`
- Candidate: `PHASE24_L10_U11_LOCAL_CORRECTION.kicad_pcb`
- Binding authority: `validation-receipts/storage-placement-corridor-authority-20260918/DECISION.md`, decision `PISXME-P24-STORAGE-PLACEMENT-CORRIDOR-20260918-R1`
- Scope: L10 moved exactly to `(143.00,127.80)`; U11/Y10/J1/anchors and protected/high-speed regions unchanged. VDDREG handoff uses In2.PWR to avoid the existing validated B.Cu USB3 corridor; no global rules or protected-bus edits.
- Target physical contacts: U11.64 LXO -> L10.1; U11.1 JMS_VDDREG_5V -> L10.2; U12.1 JMS_VDDREG_5V -> L10.2. Candidate DRC has no missing-connection entry for these pairs. Negative controls reintroduce the expected targeted missing pair when the local LXO or VDDREG candidate route is removed.
- Courtyard result: baseline had 6 courtyard-overlap violations; candidate has 5. The authorized L10/U11 overlap is removed; no new L10/U11 courtyard overlap appears.
- Native KiCad Light 10.0.6 DRC: baseline `300` violations / `499` unconnected; candidate `289` violations / `393` unconnected. Candidate classes: 124 track-width, 120 clearance, 15 copper-edge, 9 track-dangling, 7 via-dangling, 5 courtyard-overlap, 5 PTH-inside-courtyard, 2 tracks-crossing, 2 library-footprint findings. These are an integrated-board baseline with unrelated inherited findings; this receipt does not claim full-board closure.
- Negative controls: removing the candidate LXO entry creates a missing `L10.1`-to-`LXO` connection; removing the candidate VDDREG handoff creates missing `L10.2`-to-`U12.1` and `L10.2`-to-existing `JMS_VDDREG_5V` connections.
- Light image: `pisxme-kicad-light:v1`, `sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9`.
- Raw commands: `kicad-cli pcb drc --severity-all --format json --output <report> <board>`; zone fill performed with native `pcbnew.ZONE_FILLER` before candidate DRC.

This is a producer candidate for serialized Root integration and fresh-Light validation. It is not canonical until Root reconciles it against current HEAD.
