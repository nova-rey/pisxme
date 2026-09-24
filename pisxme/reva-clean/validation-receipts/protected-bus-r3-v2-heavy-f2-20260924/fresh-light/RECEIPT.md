# Fresh Light validation — Heavy v2 F2 producer candidate

- Candidate: `2c75d09edb1dccc9718c2e50dd7790dc395b77fd`
- Base: `d5a872cf`
- Image: `pisxme-kicad-light:v1`
- Image digest: `sha256:37d60e6797eaa14ea393de005b9793af5d9b5e7464aac1e4d58bec1b7803b4a9`
- Tool: KiCad `10.0.6`, fresh detached checkout
- DRC: `929` violations, `434` unconnected items
- Exact-base comparison: `920` violations, `435` unconnected items

The selected `PWR_SRC_J5_P2` raw pad is connected and one open is removed, but
DRC count increases by nine and the other F2 raw/fused pads remain open. The
candidate therefore fails integrated acceptance and is not eligible for
canonical merge. The isolated route and raw reports remain reusable evidence
for the next bounded method change.
