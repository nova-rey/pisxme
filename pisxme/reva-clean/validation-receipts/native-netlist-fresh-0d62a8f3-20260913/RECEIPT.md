# Fresh native netlist receipt

- Candidate commit: 
- Worker: qualified 
- Command: 10.0.5; input: 1 argument(s) expected. 0 provided.
Usage: export netlist [--help] [--output OUTPUT_FILE] [--variant VAR]... [--format FORMAT] INPUT_FILE

Export a netlist

Positional arguments:
  INPUT_FILE    Input file 

Optional arguments:
  -h, --help    Shows help message and exits 
  -o, --output  Output file [nargs=0..1] [default: ""]
  --variant     The variant name(s) to output, can be used multiple times to specify multiple variants.
                When specifying multiple variants, use ${VARIANT} in the output path to generate separate files for each variant.
                When no --variant argument is provided, the default variant is output. [nargs=0..1] [default: {}] [may be repeated]
  --format      Netlist output format, valid options: kicadsexpr, kicadxml, cadstar, orcadpcb2, spice, spicemodel, pads, allegro [nargs=0..1] [default: "kicadsexpr"] from the canonical schematic.
- Native export completed successfully in a fresh detached Light checkout.
- This supersedes stale checked-in SATA-era XML for current source inspection; it does not by itself close bidirectional coverage or physical connectivity.
- Raw netlist, version, validation metadata, and hashes are retained here.
