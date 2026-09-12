# Surplus-pad classification by footprint/net family

- Source commit: `139e2100`
- Worker: `pisxme-kicad-light:v1`, KiCad 10.0.6
- Surplus actual pads: 448
- J1 surplus: 393 contacts = 170 `POWER_GND`, 130 `12V_PROTECTED`, 93 no-net/unknown contacts; together with 7 schematic-expected J1 signal contacts this accounts for the 400-position J1 package.
- Other no-net/surplus pads: F1=1, F2=1, J2=8, J3=4, J4=4, J5=1, J6=1, J7=4, U7=24, U11=1, U13=1.
- Test points: TP1–TP13 each have one intentionally exposed diagnostic net.

This classifies the surplus population by owner, but no-net connector/IC contacts still require explicit no-connect/unknown disposition before the bidirectional acceptance row can close. No assignments were invented.
