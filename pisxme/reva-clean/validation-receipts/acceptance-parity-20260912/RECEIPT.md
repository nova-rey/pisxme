# Fresh integrated schematic-parity/netlist receipt

- Source checkout: current HEAD at execution; PCB candidate is the current integrated design.
- Toolchain: KiCad Light 10.0.6, qualified image.
- Native DRC with `--schematic-parity`: 340 violations / 499 unconnected items.
- Native schematic netlist export completed with return code 0; raw XML and command output retained.
- Source PCB, schematic, and rules hashes are retained in `hashes.sha256`.
- This is bounded parity/export evidence; it does not close physical connectivity or ERC/DRC acceptance.
