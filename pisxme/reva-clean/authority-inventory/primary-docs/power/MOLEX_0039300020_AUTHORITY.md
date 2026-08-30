# High-current 12 V input header authority — Molex 0039300020

Checked: 2026-08-30. Status: `CLOSED`.
The electrical selection and project-local PCB land pattern now match the exact
Molex SD-5569-002 recommended hole layout for 5569-02A2*-*.

## Candidates considered

| Candidate | Evidence | Disposition |
|---|---|---|
| Molex `0039300020` / `39-30-0020` | Molex 5569 series chart; exact DigiKey and Mouser records | **Selected** |
| Molex `39291028` | Same 5569 family, right-angle, 2 circuits, flange variant | Backup; different retention/mechanical envelope |
| Molex `26013108` | Active 5569 family, gold-plated 16-circuit variant | Rejected: excessive circuit count and no benefit for Rev-A input |

## Selected item and electrical/mechanical basis

`0039300020` is a Molex Mini-Fit Jr. 5569-series dual-row, right-angle,
2-position through-hole header with 4.20 mm pitch, tin termination, shrouded
polarized housing, and PCB retention. It mates with the 5557 receptacle family
and supports two independent contacts. Two identical board headers are reserved
for the dual 12 V input policy; each input is independently protected before the
protected-rail merge. The connector is intentionally not treated as an SMT/JLC
basic part: ordinary through-hole insertion and selective/wave/hand solder are
the assembly path.

## Procurement and lifecycle evidence

Molex lists the 5569 family as an active manufacturer series. DigiKey's exact
record reported 87,237 available for the equivalent 2-position right-angle
header, MOQ 1, about $0.75 each, and an active Mini-Fit Jr. 5569 description.
The exact Molex/Mouser family record reported 22,793 available for `39-30-0020`,
MOQ 1, about EUR0.62 each at quantity 1 and EUR0.39 at 100. Newark's exact
39-30-0020 listing reported 4,922 and a minimum of 10 at about $1.13 each;
TTI/independent supply is a further fallback but is not the primary basis.
Mating crimp housing/terminal procurement is separate and must be specified
with the cable assembly; the board header itself is the selected PCB MPN.

Sourcing risk: `LOW` for the header. It is a commodity, active, multi-channel
through-hole part with MOQ-1 availability. Assembly risk is `MEDIUM` because it
is not a normal SMT placement and requires a second solder process.

## Local reference and provenance

- Molex series authority: `https://www.molex.com/en-us/products/series-chart/5569`.
- Molex Mini-Fit Jr. connector family: `https://www.molex.com/en-us/products/connectors/wire-to-board-connectors/mini-fit-connectors`.
- Molex specification family: `https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/productspecificationpdf/555/5556/PS-5556-004-001.pdf`.
- Exact distributor records are linked in the procurement matrix and were
  captured as current web evidence; no manufacturer CAD file was redistributed.

## Exact PiSXMe decision closed

The dual cold-plug input connector selection is Molex `0039300020`, two units,
with one connector per independent 12 V input. The later PCB authoring step must
use the exact 5569-2-position drawing/ECAD pattern and keep both connectors
outside the V100 cooler reservation.

Resolved Phase 14 finding: the prior local pattern incorrectly used two
horizontal 4.20 mm-spaced electrical holes and two 2.10 mm-offset mounting
holes. The corrected local pattern uses pad 1 at (0,0), pad 2 at (0,5.50),
and one NPTH retention hole at (0,-7.30), on the opposite side of pad 1 from
pad 2: 5.50 mm between circuits 1 and 2, and 7.30 mm from circuit 1 to the
peg. Electrical and retention drills are 1.80 mm and 3.00 mm respectively,
matching the manufacturer's component-side drawing. A complete 180-degree
rotation is equivalent; the sign must not be changed independently of the
body orientation. Source: Molex `039300020_sd.pdf` / `55690002-SD`, sheet 1,
recommended hole layout for 5569-02A2*-*.
