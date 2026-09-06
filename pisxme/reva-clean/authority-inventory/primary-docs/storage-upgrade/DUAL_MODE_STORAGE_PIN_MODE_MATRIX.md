# Dual-mode storage pin and mode matrix

Status: implementation authority draft, 2026-09-06.

## Selected topology

`CM5 USB2/USB3 -> HD3SS6126RUAR USB A/B selector -> TUSB9261 SATA bridge
or JMS583-QHFA3A NVMe bridge -> HD3SS3412RUAR SATA/PCIe selector -> one
TE 1-2199230-4 Socket 3 Key-M connector`.

Both selectors and both bridges remain inside the storage island. Both bridges
are powered, but only one is connected to the CM5 USB path and only one is
connected to the shared socket high-speed paths. Mode changes are power-off
only.

## Authority

- JMS583 pin numbers: JMicron PDS-17001 Rev 2.1, retained as
  `jms583/JMS583-datasheet.txt`.
- TI selector pin and truth tables: retained HD3SS6126 and HD3SS3412
  datasheets. Both use the RUA0042A 42-pin WQFN package.
- Socket contacts: SATA-IO TP-053 v1.1 Table 4. M-key SATA lane contacts
  41/43 and 47/49 are also PCIe lane-0 PERn0/PERp0 and PETn0/PETp0.
- TE mechanical/PCB authority: 1-2199230-4 and 114-115006 Rev C.

## Mode truth table

| Mode | USB selector | storage selector | socket ownership |
|---|---|---|---|
| FORCE SATA | CM5 ↔ TUSB9261 | TUSB SATA ↔ 41/43,47/49 | SATA only |
| FORCE NVMe | CM5 ↔ JMS583 | JMS583 PCIe lane 0 ↔ 41/43,47/49 | PCIe x1 only |
| AUTO | PEDET-derived latched decision | same decision, selector polarity verified in native symbol review | SATA for SATA card, PCIe for M-key NVMe |
| empty | no bridge selected until a valid mode is established | high-speed commons isolated | no drive-presence claim |

JMS583 PCIe lane 0 is `P_RXN0/P_RXP0` pins 41/42 and `P_TXN0/P_TXP0`
pins 44/45. Clock/control are `CLKP 48`, `CLKN 47`, `P_RSTN 54`, and
`P_CLKREQN 55`; these are NVMe-local and never connect to TUSB9261. JMS583
requires 220 nF PCIe TX and 100 nF USB3 TX coupling capacitors per its data
sheet.

## Safety and ownership rules

1. USB D+/D- and USB3 TX/RX switch together; bridge USB ports are never
   paralleled.
2. SATA OOB and PCIe electrical-idle/detection are isolated by the storage
   selector; an inactive bridge is not treated as invisible.
3. `PEDET` is a SATA-versus-PCIe mode hint after exact M-key review, not proof
   of a working drive. AUTO is latched while powered down; override wins.
4. SATA A/B plus/minus names follow TP-053 and are not inferred from PCIe
   polarity names.
5. CONFIG contacts 1, 21, 69, 75; DEVSLP 38; DAS/DSS 10; SUSCLK 68; PEWAKE
   54; CLKREQ 52; REFCLK 53/55; PERST 50; and all power/ground contacts are
   explicit native connector pins. Unused host contacts are explicit NCs.

## Implementation gates

- Selector native symbols must use the TI signal tables and SEL truth tables.
- The M-key footprint is checked against TE Rev C Figure 2 and the retained
  customer DXF; the generated candidate is not parity evidence until audited.
- NVMe 3.3-V budget includes module inrush/transient and both powered bridges;
  the old SATA-only budget is not accepted as proof.
