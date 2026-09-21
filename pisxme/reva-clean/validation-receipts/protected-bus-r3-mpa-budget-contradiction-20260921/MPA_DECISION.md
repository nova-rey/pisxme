# MPA R3 Budget Contradiction

- Package: `P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER`
- Decision: `AUTHORITY_LEVEL_FAILURE`
- Fixed anchors: J5 `(12,25)`, J6 `(12,50)`, J9 `(12,75)`; F1/F4 west source pads `(29.6,13.75/16.25)` and `(29.6,38.75/41.25)`; F2/F5 at x=`57.6`; F3/F6 at x=`85.6`.
- Evidence: J5.2→F2 west pad geometric lower bound ≈42.9 mm. On released 1 oz outer copper, a 2 mm path is ≈10 mΩ at room temperature; achieving ≤0.65 mΩ would require roughly 32 mm continuous width, impossible within the 28 mm fuse spacing and holder/pad clearances. Return resistance increases the violation.
- Binding disposition: preserve J1/J5/J6/J9, nine-branch topology, 300/330 W product envelope, six-layer stack, and 8.50 mΩ complete-path gate. Supersede the derived 0.65 mΩ source-local branch-neck allocation or its associated bank spacing.
- Required next owner: Product/Power Authority to reallocate the branch resistance budget and issue consequent placement authority. No further CAD route under the current allocation is authorized.
