# RTL9210B-CG Path-B signal and mode matrix

This matrix is for the isolated qualification candidate. It records physical
socket contacts and mode ownership; it does not synthesize missing firmware or
application-circuit facts.

## High-speed mapping

| RTL9210B-CG | Shared physical function | M-key contact | SATA interpretation | NVMe interpretation |
|---|---|---:|---|---|
| 68 `SATA_TXOP/PCIE_TXOP_0` | controller TX positive | 49 | SATA-A+ | PETp0 |
| 67 `SATA_TXON/PCIE_TXON_0` | controller TX negative | 47 | SATA-A- | PETn0 |
| 64 `SATA_RXIP/PCIE_RXIP_0` | controller RX positive | 43 | SATA-B- per socket/platform naming | PERp0 |
| 65 `SATA_RXIN/PCIE_RXIN_0` | controller RX negative | 41 | SATA-B+ per socket/platform naming | PERn0 |
| 61 `PCIE_REFCLKP` | PCIe reference clock positive | 55 | unused | REFCLKp |
| 62 `PCIE_REFCLKM` | PCIe reference clock negative | 53 | unused | REFCLKn |

The SATA B-side naming is intentionally not inferred from numerical pad order.
The lane/contact mapping above is the corrected platform-side mapping. The
retained WIP root XML reverses the two lane groups and is excluded from
authority.

## Sideband and mode matrix

| Signal | Socket/control point | SATA mode | NVMe mode | Open validation |
|---|---|---|---|---|
| PEDET / CONFIG1 | M-key contact 69 to RTL pin 8 | asserted by SATA module | released by PCIe module, platform pull-up | exact pull-up, empty socket, debounce/settling |
| PERST# | M-key PERST# to RTL pin 14 | inactive/unused as defined by controller | required for endpoint reset | application-circuit timing |
| CLKREQ# | M-key CLKREQ# to RTL pin 13 | inactive/unused as defined by controller | endpoint sideband | pull-up and unpowered-state isolation |
| REFCLK | contacts 55/53 to RTL 61/62 | unused | required | coupling/termination and route basis |
| PCIe lane 1 | contacts 29/31/35/37 | not connected | not used for the single-lane Rev-A socket | final no-connect treatment from authorized circuit |
| SSD 3.3 V | M-key power contacts | required | required, with NVMe transient budget | board supply/inrush/thermal proof |
| SPI flash/config | local RTL9210B support | controller startup | controller startup | virgin programming and image rights |

## Selection behavior

The intended Path-B behavior is native PEDET SATA-versus-PCIe selection inside
RTL9210B-CG, not an external SATA/PCIe high-speed selector. A fixed CM5 USB3
connection supplies the bridge in both modes. The final design must prove that
the inactive protocol pins, SSD power, reset, CLKREQ, and REFCLK do not contend
or float unsafely in SATA mode, NVMe mode, empty-socket state, and reset.

## Qualification evidence

The following current audits pass, including intentional negative controls where
applicable:

- `phase24_rtl9210b_authority_audit.py`
- `phase24_rtl9210b_corroborating_support_audit.py`
- `phase24_rtl9210b_m2_mapping_audit.py`
- `phase24_rtl9210b_native_netlist_audit.py`
- `phase24_rtl9210b_wip_hierarchy_conflict_audit.py`

The straight-line native fixture remains rejected as route-implementation
evidence; it is not a Path-B architecture rejection.
