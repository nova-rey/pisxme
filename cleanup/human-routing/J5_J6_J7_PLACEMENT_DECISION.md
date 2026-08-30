# J5/J6/J7 placement decision

## Candidate layouts

| Candidate | Layout | Benefit | Risk | Status |
|---|---|---|---|---|
| A | Existing vertical row at `(205,12)/(205,20)/(205,28)` | Keeps current short routes | 10 mm outlines overlap at 8 mm pitch | Rejected |
| B | Vertical row at 12--14 mm pitch | Keeps one cooling edge and separates bodies | Requires low-speed reroute and room near SERVICE | Preferred for disposable trial |
| C | Horizontal row along the north edge, 12--14 mm body spacing | Maximum latch/finger access and clear differentiation | Cable exits spread laterally | Preferred fallback |

## Decision

The active 8 mm row is rejected. A safe active move requires a disposable
low-speed reroute trial with the selected mating housing. This cleanup pass
does not promote a guessed header placement into the active PCB: the current
header nets are low priority, but their exact new positions must be validated
against the SERVICE connector, board edge, and future enclosure cable exits.
