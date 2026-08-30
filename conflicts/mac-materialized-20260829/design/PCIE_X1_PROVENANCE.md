# PCIe x1 clean-room provenance

Status: observation record and design-provenance guardrail. This file documents what was studied and what may be used as evidence; it does not grant rights to redistribute third-party files.

## Clean-room rule

The future V100-to-CM5 board must start from a new, blank KiCad project. No PCB file from a routed commercial, OSHWHub, or reverse-engineered carrier may be imported, cropped, mechanically transformed, used as a tracing canvas, or edited into the project. No distinctive bend, meander, via field, component placement, or substantial layout section may be reproduced.

The design team may use the references to extract:

- logical connectivity and signal naming;
- observed connector identity and mechanical datums;
- high-level layer, plane, power-zone, and manufacturing lessons;
- publicly documented CM5 electrical requirements;
- independent physical constraints for our own one-lane board.

The resulting x1 architecture deliberately changes the problem: no PCIe card edge, one lane, CM5 adjacent/under the former edge region, and a newly derived corridor.

## Evidence classes

| label | meaning | allowed design use |
|---|---|---|
| OBSERVED | read directly from a source file, live KiCad state, or image | quote as an observation; do not treat as a passing design |
| AUTHOR CLAIM | statement by an author/seller/project maintainer | record with attribution; never use alone as an electrical guarantee |
| INFERRED | conclusion derived from observations | use as a hypothesis, marked for validation |
| SPEC-DERIVED | official Raspberry Pi, PCI-SIG, or fab documentation | use to set requirements, subject to endpoint compatibility |
| UNKNOWN | insufficient evidence | do not silently fill with a reference-board assumption |

## Primary SXM2 source

| source | acquisition/pin | what was used | what was not used |
|---|---|---|---|
| [bbenchoff/SXM2toPCIe](https://github.com/bbenchoff/SXM2toPCIe) | immutable clone at `/Users/Cooper/Documents/ChatGPT/sxm2/references/SXM2toPCIe`; commit `3173b02c085218d66c4a2a9e5492853fb53ee097`; acquired 2026-08-20 | J2/J3 connector identity, source pin map, net names, partial lane landmarks, declared stackup, KiCad parse/DRC/ERC evidence | no PCB geometry, no trace coordinates, no via placement, no component placement, no claim that its copper is a complete high-speed route |
| [Benchoff reverse-engineering article](https://bbenchoff.com/pages/SXM2PCIe.html) | accessed 2026-08-20 | author-reported SXM2 pin table, `PERST#` E18, populated single Meg-Array, absent NVLink connector, conventional slot presence tie, power/fan observations | no NDA material, no unverified undocumented pin behavior treated as fact |
| [l4rz field report](https://l4rz.net/running-nvidia-sxm-gpus-in-consumer-pcs/) | accessed 2026-08-20 through Benchoff link | independent evidence that commercial SXM2-to-PCIe adapters have been operated with V100-class modules; high-level connector/power context | no layout copying; photographs are not measurements of our board |

The primary KiCad source was opened and inspected through KiCad 10.0.5 in a separate working copy. The live bridge reported 38 footprints, 1,104 pads, 129 tracks, 7 vias, 5 zones, 429 graphics, 558 nets, and four copper layers. DRC reported 73 violations and 285 unconnected items; ERC reported 472 violations. These are **OBSERVED** properties of that source and remain unmodified.

The source's lane-0 route is incomplete: only partial edge/capacitor-row copper exists. Its 0.1016 mm/0.127 mm `PCIe_Diff` class is not an impedance proof, has no explicit length/skew/impedance constraints, and does not consistently match post-coupling net names. This is why the source is a pinout/mechanical/topology reference, not a known-good high-speed layout.

The source repository has no root `LICENSE` file in the pinned commit. Benchoff's article states that the hardware files are WTFPL 3.0 and the article text is CC-BY-SA-4.0; the embedded SnapMagic model file has separate terms. This project preserves the clone as immutable reference material and does not redistribute or modify its files in the new design.

## Additional SXM2 carrier evidence

| source | status | extracted fact | classification and limit |
|---|---|---|---|
| [LiuXinyu12378/SXM2_to_PCIE_adapter](https://github.com/LiuXinyu12378/SXM2_to_PCIE_adapter) | shallow clone at `/Users/Cooper/Documents/ChatGPT/sxm2/references/LiuXinyu12378-SXM2_to_PCIE_adapter`; commit `27dd1229889f4f0c03324b419931d2d466fccde4`; no license file found | README claims V100/P100 compatibility, x16 operation, 3×8-pin plus PCIe power with theoretical 525 W, and offers 4-layer and 6-layer ENIG boards; photographs show high-current connectors and a separate power module on one revision | README performance/power claims are **AUTHOR CLAIM**; photographs are **OBSERVED** high-level placement/power evidence only; no route geometry or coordinates used |
| [OSHWHub routed/tested carrier](https://oshwhub.com/chenrunyu/sxm2-pcie-adapter-turbo-fan-vers) | direct OSHWHub fetch was unavailable with HTTP 403; reviewed the linked [LCSC article](https://www.szlcsc.com/info/16304.html) and its photographs | article states P100/V100/A100 support, 300 W+ power, active cooling, NVLink extension, TPS56624x regulator, LMK00334 level converter; photographs show a real fabricated board | performance and topology statements are **AUTHOR CLAIM**; image observations are coarse and not layout measurements; no source geometry imported |
| [current commercial six-layer listing](https://www.ai-cooling.com/?product=198) | seller page accessed 2026-08-20 | seller claims dual 6+2-pin power, 300 W tested without downclocking, six-layer impedance optimization, and zero signal loss | **AUTHOR CLAIM** only; not used to set trace width, impedance, or current capacity |

These routed/fabricated references are corroboration that power delivery, cooling, and controlled high-speed construction are real design concerns. They are not templates for our board.

## Official CM5 sources

| source | use | classification |
|---|---|---|
| [Raspberry Pi CM5 datasheet](https://datasheets.raspberrypi.com/cm5/cm5-datasheet.pdf) | PCIe Gen2 host limitation; optional/unsupported Gen3; TX/RX crossing for direct IC connection; 220 nF AC-coupling ownership; 90 Ω; 0.1 mm within-pair match; required `CLKREQ#` and `PERST#`; `WAKE#` software limitation; CM5 pins 102, 104, 106, 109–124; module mechanics | **SPEC-DERIVED** |
| [Raspberry Pi CM5IO datasheet](https://datasheets.raspberrypi.com/cm5/cm5io-datasheet.pdf) | official carrier block diagrams, M.2 sideband topology, 5 V CM5 power context, and official reference-design status | **SPEC-DERIVED / OBSERVED** |
| Raspberry Pi official CM5IO revision-2 KiCad archive, acquired 2026-08-20 from the [official design-files page](https://pip.raspberrypi.com/categories/1098-design-files) | preserved locally at `/Users/Cooper/Documents/ChatGPT/sxm2/references/RaspberryPi-CM5IO-rev2`; ZIP SHA-256 `48b14a6757b0edc0ac110331445f35a4212b5ce432bdcec6605c99431b59496b`; inspected `CM5IO.kicad_pcb`, `CM5IO.kicad_pro`, and PCIe schematics | official 4-layer example uses 1.6 mm board data and a `90R` class with 0.147 mm width, 0.253 mm differential gap, 0.45/0.20 mm vias; its M.2 schematic connects `CLKREQ#`, `WAKE#`, `PWR_EN`, and `PERST#` to CM5. These are **OBSERVED official reference-design facts**, not copied geometry |

KiCad CLI 10.0.5 successfully parsed the official CM5IO schematic and exported a netlist. It also parsed the board and produced a DRC report with 67 violations and 0 unconnected items in this environment. Those DRC results are not a cleanliness claim about the official design and were not used to change it.

The official CM5IO design archive is kept outside the outer Git history and ignored as a large reference. Its local presence does not change the clean-room rule.

## Official PCIe and fabrication sources

| source | use | classification |
|---|---|---|
| [PCI-SIG PCIe 2.0 FAQ](https://pcisig.com/faq?field_category_value%5B%5D=pci_express_2.0) | 2.5/5.0 GT/s backward-compatible Gen2 behavior | **SPEC-DERIVED** |
| [PCI-SIG PCIe generation FAQ](https://pcisig.com/faq?field_category_value%5B%5D=pci_express_3.0) | 8.0 GT/s Gen3 context and manufacturability tradeoff | **SPEC-DERIVED** |
| [JLCPCB impedance-calculator guide](https://jlcpcb.com/help/article/user-guide-to-the-jlcpcb-impedance-calculator) | official input model: finished thickness, copper weights, target impedance, pair spacing, layer, and reference planes | **SPEC-DERIVED** |
| [JLCPCB controlled-impedance stackup reference](https://jlcpcb.com/impedance) | published 4-layer and 6-layer impedance-control stackup families | **SPEC-DERIVED**, subject to current fab quotation |
| [PCBWay standard layer-stack reference](https://www.pcbway.com/pcb_prototype/What_is_layer_stack_up.html) | alternative mainstream-fab stackup comparison | **SPEC-DERIVED**, subject to current fab quotation |

No production trace width is taken from a search result, photograph, or reference PCB. The final width/gap will be generated from the selected fabricator's current laminated stackup and impedance coupon request.

## Independent derivations recorded in this phase

1. **Lane 0 candidate:** lane 0 is the leftmost/topmost and shortest natural route to the former edge region in the source geometry. This is an **INFERRED** placement convenience, not a claim that the source lane is routed or electrically validated.
2. **CM5 placement:** adjacent CM5 is provisionally preferred for access, cooling, and assembly; underside CM5 remains plausible if the 4.0 mm connector/2.5 mm underside-clearance option and V100 cooler envelope permit it. **INFERRED / UNKNOWN.**
3. **Six layers:** six layers are recommended primarily for the 300 W-class power distribution and clean ground planes, not because one short Gen2 lane needs x16-style escape density. **INFERRED.**
4. **No redriver/retimer:** a short Gen2 x1 channel does not presently justify an active repeater. Add one only after SI/bring-up evidence. **INFERRED.**

## Forbidden provenance shortcuts

- Do not copy the Benchoff, OSHWHub, Liu, l4rz, or seller-board PCB into a new project.
- Do not crop the former card-edge area and call it the x1 starting layout.
- Do not reproduce distinctive commercial bends, meanders, via rows, fanouts, or power placement.
- Do not infer that multiple commercial boards independently prove a detail if they may share one source design.
- Do not call a seller's “zero signal loss,” “300 W tested,” or “stable” statement a measured SI/current rating.
- Do not call the pinned Benchoff PCB a completed routed reference; live DRC and track evidence contradict that interpretation.

## Provenance gate for the next phase

The next KiCad phase may create a new schematic and mechanical study only after this document and [PCIE_X1_DERIVED_REQUIREMENTS.md](PCIE_X1_DERIVED_REQUIREMENTS.md) are accepted as the design authority. The new layout must be independently generated around the x1 topology, CM5 placement, chosen stackup, and V100 power/thermal constraints.

## Phase 2: interface and mechanical provenance

The official CM5 electrical and mechanical data used for the interface contract were obtained from the [CM5 datasheet](https://datasheets.raspberrypi.com/cm5/cm5-datasheet.pdf), [CM5IO datasheet](https://datasheets.raspberrypi.com/cm5/cm5io-datasheet.pdf), [firmware overlay documentation](https://github.com/raspberrypi/firmware/blob/master/boot/overlays/README), and the [official Raspberry Pi design-files page](https://pip.raspberrypi.com/categories/1096-design-files). The CM5 STEP ZIP was preserved locally at `/Users/Cooper/Documents/ChatGPT/sxm2/references/RaspberryPi-CM5-step/`; its SHA-256 is `2b4d26c6b30607c68099ad60df6fb8b8c8d04e9461f325c7c77dc421d2855005`.

The independent schematic at `/Users/Cooper/Documents/ChatGPT/sxm2/pisxme/PiSXMe.kicad_sch` was created from KiCad's generic blank EuroCard template, not from any SXM2 carrier or CM5IO schematic. The template supplied only the KiCad document container; the interface text, nets, coupling components, local clock-request policy, and power/debug notes were authored for this project. No reference PCB geometry, routed pair, via field, component placement, or restricted layout fragment was imported.

Public NVIDIA data was used only to bound the V100 power/mechanical risk. The [V100 datasheet](https://images.nvidia.com/content/technologies/volta/pdf/tesla-volta-v100-datasheet.pdf) identifies the SXM2 system interface as NVIDIA NVLink and gives a 300 W-class maximum for the SXM2 product; it does not publish the reverse-engineered standalone PCIe clock/sideband contract. That gap is recorded as a bring-up gate rather than filled from commercial geometry.
