# JMS578 procurement and firmware evidence

Date checked: 2026-08-29. This is an authority record, not a schematic.

JMicron's product page and brief identify `JMS578`, USB 3.1 Gen1 to SATA 6
Gb/s, BOT/UASP, external SPI NVRAM, 30 MHz crystal, internal 5 V to 1.2 V and
3.3 V regulation, and QFN-48 6 x 6 mm. The locally preserved brief is
`../JMS578.pdf`, SHA-256
`3c59d77780a50314462e8967ec91e9fe532d1356becd31a7b9945b66410e1ae0`.

LCSC lists the exact bare device as `C17700079`, MPN `JMS578`, QFN-48(6x6),
minimum 1, standard pack 1000, reference price $0.4948 at quantity 1 and
$0.1876 at quantity 1000, but the live product record says **Out of Stock**.
The JMicron brief says software utilities download upgraded firmware under USB
2.0/3.0 and SPI NVRAM carries VID/PID customization, but publishes no image,
image license, configuration format, pin-level design guide, or public
programming-tool download.

ASM1153E was evaluated as the mature alternative. ASMedia documents the same
QFN-48 6 x 6 class, USB3.2 Gen1-to-SATA6G, BOT/UASP, SPI NVRAM and crystal
options. No dependable bare-chip major-distributor buy record surfaced. A
StarTech ASM1153E product is a real assembled module, but its datasheet says
TRIM is not supported; legacy firmware tooling is proprietary/discontinued.

The local MiSaKa and EEWorld captures support the usual crystal, SPI memory,
reset, and decoupling topology only. They do not establish a distributable
firmware package or exact Linux UAS/TRIM/reset behavior for PiSXMe.

Decision: `PHASE2_AUTHORITY_BLOCKED`. Before integrating a bare bridge, obtain
the exact firmware image and redistribution right, SPI image format, VID/PID
and serial procedure, USB descriptors, UAS/BOT and TRIM behavior, Linux
suspend/resume and reset behavior, and a sample for destructive reset testing.
No firmware image is present here and none will be fabricated from secondary
captures. The practical replacement is a purchased assembled USB-to-M.2-SATA
module with explicit firmware/Linux support, or removal of integrated SATA
bridging from Rev A. A bare ASM1153E substitution is not a closure.

Provenance: JMicron and ASMedia manufacturer pages/briefs; exact LCSC listing;
StarTech product datasheet; Plugable legacy-firmware warning; local secondary
captures retained as observations only.
