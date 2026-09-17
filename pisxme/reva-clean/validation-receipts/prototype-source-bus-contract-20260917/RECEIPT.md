# Receipt — P24-PROTOTYPE-SOURCE-BUS-CONTRACT

- Package: `P24-PROTOTYPE-SOURCE-BUS-CONTRACT`
- Contract: `PISXME-P24-PROTOTYPE-SOURCE-BUS-20260917` revision `1.0.0`
- Base SHA: `c2e0194c432e712d6f8386b9682f038dd06188e6`
- Result: `DONE` for the delegated authority-artifact scope
- CAD changed: no
- Six-loop limiter work resumed: no
- Phase 25/26 work: no

## Closed criteria

- 300 W sustained / 330 W for 100 ms retained.
- 12.0 V nominal, 11.4–12.6 V source window and 40 A continuous / 45 A, 100 ms source capability bound.
- 11.05 V sustained / 11.00 V peak protected-bus minimum and 12.60 V maximum bound.
- Complete positive-plus-return source-to-J1 path cap of 10.0 mOhm, with explicit harness, protection, PCB, and J1 allocations.
- Connector/conductor ampacity, common-bus return, via-array, copper, thermal, ordinary protection, and no-sharing requirements recorded.
- Prototype-only first-power validation, stop criteria, and unresolved empirical behavior are explicit.
- Superseded six-loop requirements are not reintroduced.

## Validation performed

`PROTOTYPE_SOURCE_BUS_CONTRACT.json` parses with Python `json`; all referenced source files were hashed into the JSON evidence map; calculation values were recomputed from the stated 300/330 W, 22.7 W, 90%, 11.4 V and 10 mOhm inputs. No PCB, schematic, library, rules, configuration, or queue file was edited.

The contract is a design-validation authority artifact. It does not claim fabricated measurements, hardware operation, vendor authorization, or production qualification.
