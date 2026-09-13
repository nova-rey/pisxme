# Fresh ERC validation — footprint library context

Candidate: `737b8191`; qualified `pisxme-kicad-light:v1`; command:
`kicad-cli sch erc --severity-all --format json --output erc.json
--exit-code-violations PiSXMe_RevA_Clean.kicad_sch`.

Result: 293 violations, return code 5. This reproduces the source-context
correction's reduction from 296 to 293 findings and removes the three
footprint-link findings. The integrated ERC acceptance row remains open.
