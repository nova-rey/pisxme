# Phase 24 storage TX support V132 receipt

V132 selectively translated only the saved isolated TX coupling-cap support
legs onto V127, moved C86/C87 coherently, and attempted a local PERST duck.

Native DRC rejected the candidate at 150 violations / 499 opens. The real
failures are a CM5_PERST-to-BRIDGE_3V3 short at TP5, a PERST crossing with
the translated USB_TXP1 path, and a JMS_USB3_TXP/TXN local clearance issue.
The candidate is rejected. Its endpoint topology remains useful, but the
saved y=150 support corridor is not transplantable through the live TP5 and
PERST geometry; the next route must shift that corridor and revalidate the
affected single-ended PERST path.
