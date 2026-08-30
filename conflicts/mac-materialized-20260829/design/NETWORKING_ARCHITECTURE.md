# Networking architecture

Native RJ45 is omitted from PiSXMe Rev A. FAST B is reserved as a native CM5 USB3 host port for a commodity USB 2.5GbE adapter.

## Why this is practical

USB3 Gen1 provides a 5Gbps physical link, enough headroom for a 2.5GbE adapter after protocol overhead. Real throughput is adapter-, host-load-, driver-, and enclosure-dependent; the design does not promise line-rate 2.5GbE.

Common adapters use Realtek RTL8156/RTL8156B-class or ASIX 2.5GbE USB3 controllers. Linux support is generally available in modern kernels, but the deployed CM5 image must include the relevant driver and firmware behavior. Adapter thermals and link negotiation remain external deployment concerns.

FAST B has its own CM5 USB3 port 1 pins. FAST A can simultaneously host storage on USB3 port 0 without sharing a single USB hub upstream. The V100 still uses the independent PCIe Gen2 x1 link.

## Mechanical consequence

Removing RJ45 avoids magnetics, high-speed Ethernet routing, a large board-edge connector, and a fixed enclosure cutout. Builders may use direct onboard USB-C, a short panel-mount USB-C extension, or an internal adapter.

The board does not require Wi-Fi. A CM5 SKU with optional Wi-Fi can be used, but Ethernet remains an explicit external USB accessory.

Confidence: CM5 USB-port independence is official Raspberry Pi documentation; practical 2.5GbE compatibility is an ecosystem/driver conclusion and should be tested with the chosen adapter during deployment.
