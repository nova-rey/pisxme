# Cooling-control recommendation

Rev-A should expose three standard 4-pin headers:

- `J5` fan 1: 12 V, GND, tach, PWM.
- `J6` fan 2: 12 V, GND, tach, PWM.
- `J7` pump/aux: 12 V, GND, tach, PWM, with a cooler-specific current limit.

The selected header family is JST `B4B-XH-A`, 2.50 mm pitch. The board should
provide local bulk/decoupling and a documented current limit, but it should
not promise that the raw V100 12 V rail can start an arbitrary pump. A later
power review may add a separate protected pump branch or a soft-start switch.

For Rev-A, CM5 software control is preferred over adding an MCU: it avoids a
new firmware/update path and is sufficient for a non-safety-critical prototype
if the system has a hardware thermal shutdown independent of fan software.
Use the tach inputs for monitoring and PWM for command. A dedicated fan
controller or external pump controller remains a user-defined option for an
enclosure that must regulate cooling while CM5 is off or booting.

Do not place high-speed probe points or stubs in the PCIe/REFCLK corridor. If a
future thermal monitor is needed, add low-speed sensor headers in the cooling-
control zone.
