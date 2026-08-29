# SKiDL spike fixtures

These small source files preserve the Mac-side SKiDL experiments used to test
electrical-authority generation. They are disposable fixtures, not PiSXMe
source and not release artifacts.

Known environment from the experiment: Python 3.11, SKiDL 2.3.0,
kinet2pcb 1.1.4, KiCad 10.0.5. The flat fixture generated a KiCad schematic
and netlist and its disposable PCB mapping was structurally correct. The
hierarchy fixture did not close the native ERC/hierarchy gate; do not treat it
as proof of hierarchical authority. Reproduce on Linux before using SKiDL for
M6.

Some generated outputs may remain in the ignored local `work/skidl_spike/`
directory, but they are not required for a clone. Re-run the checked-in source
files to regenerate them. Do not copy virtual environments or caches into the
repository.
