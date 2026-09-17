# Receipt — ADM1175 limiter authority reassessment

- Package: `P24-ADM1175-LIMITER-AUTHORITY-REASSESSMENT`
- Base SHA: `578b55d7`
- Review SHA: `02334352a16321a28f52f4b4c579aa8030f6d6ec`
- Result: `DONE_WITH_RESIDUAL_AUTHORITY_DEPENDENCY`
- Authority status: `CANDIDATE_REJECTED_FOR_BINDING`
- Dependency retained: `authority:6A-limiter-qualification`
- CAD changed: `no`
- Product envelope changed: `no`

Product / Power Authority reviewed the Librarian ADM1175 packet and the
Analog Devices Rev. C primary datasheet. The 16.13 mOhm screening shunt
calculates to 6.0037330222--6.3961705444 A under its stated assumptions,
but the exact shunt, hot external FET/path, reverse and fault-energy
coordination, thermal installation, and production calibration/test contract
remain open. Neither ADM1175 variant is promoted. The HPQ4 six-loop and
300 W / 330 W product requirements remain unchanged.

The complete signed disposition and resumption evidence are in
`ADM1175_LIMITER_AUTHORITY.json`; no CAD or product-envelope edit is
authorized. This is an internal authority dependency, not an external blocker.
