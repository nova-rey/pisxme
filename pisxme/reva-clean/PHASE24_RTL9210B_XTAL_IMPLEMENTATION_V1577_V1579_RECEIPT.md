# Path-B fixed-orientation crystal implementation cycle — V1577–V1579

Status: route candidates rejected; orientation unchanged

These experiments all use Claude's accepted 0° RTL9210B baseline and do not
reopen the orientation decision.

| Candidate | Result | Disposition |
|---|---|---|
| V1577 southwest corridor | 6 DRC findings / 2 REFCLK opens; XTAL_IN crossed RTL_1V1/PCIe and shorted the existing RTL_3V3 transition | rejected |
| V1578 rehomed RTL_3V3 + XTAL_IN | 7 findings / 2 REFCLK opens; removed the RTL_3V3 short but retained two corridor crossings and a local clearance issue | rejected |
| V1579 farther-west corridor | 6 findings / 2 REFCLK opens; no XTAL_IN net short, but XTAL_IN crosses XTAL_OUT and RTL_1V1, with a local RTL_3V3 clearance/dangling-tail issue | rejected |

The experiments validate the implementation diagnosis: the remaining issue is
coordinated source-field and support-corridor allocation under the fixed 0°
package orientation. They do not show that another orientation is better.
The next implementation pass must co-author the crystal, RTL_3V3 transition,
and adjacent return/PCIe corridors, preserving U1's fixed orientation and the
approved layer/via contract. No Path-A or production board was modified.
