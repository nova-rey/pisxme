# JMS581DL substitution review

Checked 2026-09-06. JMS581DL was investigated after JMS583 because it could
collapse the two-bridge/two-selector architecture into one controller.

## What is confirmed

JMicron's official product page and Product Brief PDB-00000012 Rev 1.00
identify JMS581DL as USB 3.2 Gen 2 to either SATA 6 Gb/s or PCIe NVMe Gen3 x2,
with automatic protocol switching, UASP/BOT, TRIM for both paths, and a
144TFBGA 9 x 9 mm package. JLCPCB lists `JMS581DL` as assembly part
`C9900187649`, with a 144-ball 0.75-mm BGA library and X-ray-required SMT
assembly.

Sources:

- https://www.jmicron.com/products/list/18
- https://www.jmicron.com/file/download/1222/JMS581DL%2BProduct%2BBrief%2B%28Rev.1.00%29.pdf
- https://jlcpcb.com/partdetail/JLCPCBAssembly-JMS581DL/C9900187649

## Why it is not selected

The public JMicron brief has no ball-by-ball signal assignment, escape/land
pattern, reference schematic, detailed power/reset/clock/flash requirements,
firmware image, programming utility or programming rights. JLC's library is
assembly evidence, not manufacturer electrical authority. The BGA is also a
materially harder ordinary-prototype assembly than the JMS583 QFN64.

JMS581DL therefore does not beat JMS583 under the project gate. It remains a
credible architecture fallback if JMicron supplies the design pack and
firmware/supply terms, but no JMS581DL symbol, footprint, or PCB wiring is
promoted from this review.
