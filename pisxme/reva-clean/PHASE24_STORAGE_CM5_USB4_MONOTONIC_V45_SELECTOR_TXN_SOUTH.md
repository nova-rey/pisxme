# Phase 24 Path-A V45 selector-side TX_N experiment

**REJECTED — route implementation experiment.** V45 regenerated only the
TUSB9261/HD3SS3412 SATA TX pair from V41, retaining ordinary-via transitions
at both ends and moving TX_N below the VBUS via field exposed by V44.

Native DRC: **601 violations / 399 unconnected items**. The complete SATA
endpoint connectivity audit passes. The VBUS short introduced by V44 is
absent, but native DRC reports one real inherited-region short:
`CM5_USB3_TX_N` to `CM5_REFCLK_P` at `(72.0,106.3)`. No severity or layer
policy changed. V41 remains the best disposable parent because its saved
report has 599 violations / 399 opens with zero shorting entries.

Next, coauthor the CM5 USB3 TX_N transition and selector-side SATA corridor;
do not promote V45 or restore its copper to production authority.
