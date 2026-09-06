# TE M-key Socket 3 authority

Candidate: `1-2199230-4`, TE Connectivity 67-position, 0.5-mm pitch, 4.2-mm
height, right-angle SMT, M code, gold contact finish.

## Manufacturer evidence

TE's exact product page identifies the part as Active, M code, 67 positions,
SMT, 4.2 mm height, 50 VAC and 0.5 A per contact, with customer 2D/3D CAD
links and application specification `114-115006`:

https://www.te.com/de/product-1-2199230-4.html

The retained LCSC datasheet is a procurement corroboration only. TE's
application specification is captured at:

https://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocFormat=pdf&DocLang=English&DocNm=114-115006&DocType=Specification+Or+Standard&PartCntxt=1-2199230-4

Local file: `TE-114-115006-application-spec-revC.pdf`.

The application spec states that the M.2 connector accepts standard modules,
is designed for automatic placement, requires precisely located PCB pads,
and gives reflow, insertion and removal guidance. TE's exact customer drawing
and CAD files must still be imported into the project library for final
pad/courtyard/3D parity; the family application layout is not a substitute
for that final comparison.

## Procurement and decision

DigiKey carries the exact MPN with MOQ 1 and a displayed quantity-1 price of
approximately $2.11 in the captured page, but the page showed factory lead
time rather than dependable immediate stock. TE's page currently says the
part is not available and directs buyers to TE/distributor support. Sourcing
risk is MEDIUM. The exact MPN is preferable to the existing JAE B-key part,
but it is not production-closed until the customer drawing/CAD and a current
prototype quote are retained.

Decision: replace the existing B-key J3 only after exact M-key contact/pad
mapping, 2280 retention geometry, courtyard, and procurement checks pass.

## Provenance

TE material is retained as manufacturer reference documentation. The LCSC
copy is labeled corroborating procurement evidence and is not used as the
land-pattern authority.
