# Power limiter selection authority receipt

Package `P24-POWER-LIMITER-SELECTION-AUTHORITY` returned
`NO_QUALIFIED_PRODUCTION_MPN` at review base
`a5572d6a02e94cf349e4619c5c07bae9bc31ca78`.

The signed HPQ4 contract requires six independent loops, each guaranteed at
6.000--6.400 A, with a hot limiter allocation no greater than 57 mOhm. The
retained MAX17527A and TPS1663 options fail the current-window proof; retained
controller, nFET, fuse, and TVS parts are not active limiter options. No MPN,
source contract, footprint, or CAD change is authorized.

The exact resumption dependency is
`knowledge:authoritative-6A-window-limiter`: Librarian must search/index a
manufacturer-qualified limiter or commission bounded Researcher acquisition,
then Product/Power Authority must issue a new binding selection. This is a
scoped internal dependency, not a campaign-wide blocker.
