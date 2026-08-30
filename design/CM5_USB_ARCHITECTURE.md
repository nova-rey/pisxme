# CM5 USB architecture

Status: **Rev-A architecture resolved; PCB remains placement-only and unrouted.**

Primary authority: Raspberry Pi, [Compute Module 5 datasheet](https://pip.raspberrypi.com/categories/944-raspberry-pi-compute-module-5/documents/RP-008180-DS/cm5-datasheet.pdf?disposition=inline), and [Compute Module documentation](https://www.raspberrypi.com/documentation/computers/compute-module.html).

## Confirmed CM5 interfaces

| PiSXMe port | CM5 pins | CM5 function | Intended role |
|---|---|---|---|
| USB-C FAST A | 128/130 RX, 134/136 D+/D-, 140/142 TX | USB3 port 0 | USB 3 storage |
| USB-C FAST B | 157/159 RX, 163/165 D+/D-, 169/171 TX | USB3 port 1 | USB 3 Ethernet adapter |
| USB-C SERVICE | 103/105 D-/D+, 101 USB_OTG_ID | independent USB2 | host/service and recovery |
| CM5 control | 111 VBUS_EN, 93 nRPIBOOT | USB power enable and boot strap | fast-port power / rpiboot procedure |

The datasheet specifies two independent USB3 interfaces, each capable of 5Gbps and capable of simultaneous operation, plus one independent USB2 high-speed interface. The PCIe interface is a separate Gen2 x1 host interface; the USB architecture does not consume PCIe bandwidth.

FAST A and FAST B are therefore not two connectors behind a hub or a shared USB upstream link. Each has its own CM5 SuperSpeed TX/RX pair, USB2 companion pair, Type-C CC/source controller, SuperSpeed orientation mux, VBUS switch, two four-line `TPD4EUSB30` SuperSpeed ESD arrays (one per orientation branch), and one `TPD2EUSB30A` USB2 companion-pair ESD array. The companion D+/D− pair is required to terminate the USB3 Type-C port correctly; it is not the separate CM5 USB2 interface.

## SERVICE role

SERVICE is a USB2-only Type-C dual-role port using `TUSB320LAIRWBR`. In normal appliance operation it is configured as a host and can drive a small hub or keyboard/mouse. For CM5 provisioning, the board exposes the CM5 USB2 path and preserves `nRPIBOOT` and internal UART access. Raspberry Pi's documented flow is to assert `nRPIBOOT`, connect the USB slave path to a host, run `rpiboot`, and use the resulting mass-storage gadget to provision eMMC.

The service VBUS switch is hardware-interlocked with the TUSB320 ID/status signal. It is enabled only when the CM5 is acting as a source/host, preventing VBUS backfeed when the port is used as a device for recovery. The exact bootloader/firmware mode remains a bring-up configuration item; the schematic does not claim that a single port can simultaneously be host and device.

CM5 USB2 host mode can be selected with the documented `dtoverlay=dwc2,dr_mode=host` configuration. The internal UART remains available even if SERVICE is occupied or USB enumeration fails.

## Important constraints

- CM5 pins 94/96 are CM5 power-input PD CC pins, not the external USB port CC pins; they are not reused here.
- CM5 pin 111 is a 3.3V active-high USB3 power-enable control shared by the two fast-port source switches.
- CM5 USB3 TX coupling is internal per the datasheet; no second external TX capacitor is added.
- USB3 and USB2 are routed as 90-ohm-class interfaces. USB3 reversible orientation is handled by `HD3SS3212`; USB2 does not need a SuperSpeed mux.
- No USB hub, native RJ45, USB-PD profile, or microSD slot is added.

## Confidence

CM5 interface count, pin numbers, independence from PCIe, and USB2 OTG/recovery signals are **official Raspberry Pi documentation**. SERVICE dual-role implementation is an engineering implementation using TI's Type-C controller and hardware VBUS interlock; it still requires Rev-A software/bring-up validation.
