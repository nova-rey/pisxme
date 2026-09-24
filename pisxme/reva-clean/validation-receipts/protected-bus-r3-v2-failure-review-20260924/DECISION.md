# Protected-bus R3 v2 failure review and next method

- Failed candidate: `2c75d09e`
- Base: `d5a872cf`
- Scope: J5.2 `PWR_SRC_J5_P2` to native F2 raw pad
- Result: one open removed, but fresh Light DRC rose from 919 to 929

The added findings localize to the first via at `(16.276786,23.762484)`: it is
within the J5.2 drilled-hole clearance envelope and violates the surrounding
GND zones; the route also leaves a dangling B.Cu endpoint. This is an
implementation geometry failure, not a contradiction of the MPA R3 cohort.

Next bounded method: retain the same GUI-native interactive route and exact
endpoint/layer contract, but place the ordinary source via farther along the
authorized source corridor near `(24.5,24.5)` after a short F.Cu escape. The
interactive router must obstacle-avoid the J5 hole/zone, continue on In2.Cu to
F2 raw `(57.6,13.75)`, and finish the route with no dangling endpoint. No
placement, layer-role, rule, or product constraint changes are authorized.
