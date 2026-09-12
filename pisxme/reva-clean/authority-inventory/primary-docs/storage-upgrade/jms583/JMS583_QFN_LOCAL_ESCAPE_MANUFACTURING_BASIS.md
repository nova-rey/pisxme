# JMS583 local QFN escape manufacturing basis

Date: 2026-09-12  
Status: `SELECTED_LOCAL_EXCEPTION`

## Selected rule

The immediate JMS583/Y10 crystal escape uses 0.10 mm trace width and 0.10 mm
copper clearance. It uses no new vias. All routing outside the immediate
U11/Y10 escape returns to the normal project geometry; the VDDREG and LXO
branches retain 0.15 mm traces and ordinary 0.60/0.30 mm through-vias.

## Fabrication basis

The retained JLCPCB capability evidence in
`authority-inventory/rtl9210b/RTL9210B_QFN_LOCAL_ESCAPE_MANUFACTURING_BASIS.md`
records a 0.09/0.09 mm multilayer 1-oz trace/space minimum and 0.10 mm
pad-to-track minimum. The selected 0.10/0.10 mm copper rule is therefore the
least aggressive rule that clears the measured 0.4 mm-pitch JMS583 pad field
while remaining inside the stated prototype fabrication capability. The
candidate does not use the tighter via capability; it keeps the ordinary
through-via contract.

## Scope control

The companion KiCad rule is net-gated to `XIN` and `XOUT`, which are local
crystal nets, and the saved-board scope audit checks that every such track is
inside the immediate U11/Y10 escape window. No global netclass minimum is
changed and no severity is waived. Native DRC remains responsible for all
other board rules and reports inherited findings separately.

## Provenance

Package and pin authority remain the JMicron brief/datasheet and the reviewed
local land-pattern record. Fabrication capability is the retained current JLCPCB
capability capture. This document records a bounded manufacturing decision; it
does not replace native DRC or physical prototype verification.
