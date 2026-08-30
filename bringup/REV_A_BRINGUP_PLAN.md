# PiSXMe Rev-A bring-up plan

Status: `PLANNING ONLY — DO NOT APPLY UNTIL RELEASE GATES CLOSE`

## Before installing CM5 or V100

1. Inspect the assembled board under magnification, especially the SXM2,
   CM5, HD3SS3212/DQA, USB-C, fuse, and Mini-Fit Jr joints.
2. Verify board revision, connector orientation, fuse values, R1 assembly
   choice, and cooler/backplate clearances.
3. Measure resistance from raw 12 V, protected 12 V, CM5 5 V, USB 5 V, and
   3V3 to ground. Do not power through an unexplained low resistance.
4. Check both input branches independently for shorts and correct fuse
   continuity. A single-branch-loss condition is an abort condition for a
   300 W V100 test.

## Current-limited power checks

Use a current-limited regulated 12 V source. With the V100 and CM5 absent,
verify raw/protected 12 V, CM5 5 V, USB 5 V, control enables, and regulator
temperature. Confirm SERVICE VBUS is disabled before connecting an external
recovery host.

## CM5-only bring-up

Install the CM5 with cooling/support hardware in place. Use the internal UART
first. Verify boot from eMMC on the recommended CM5 SKU, SERVICE USB2 host
operation, FAST-A/FAST-B USB3 enumeration, USB storage, USB Ethernet adapter,
fan/pump outputs, reset, and the documented `nRPIBOOT` recovery procedure.

For recovery/device mode, disable the board-side SERVICE VBUS source before
connecting the external provisioning host. Do not assume automatic role
handoff is safe until measured.

## V100 bring-up

Only after the host and cooling control are stable:

1. Install the V100 and cooler.
2. Verify both 12 V input branches are present and current-limited.
3. Confirm fans/pump are running before GPU enable.
4. Check PCIe enumeration with `lspci`.
5. Check the NVIDIA driver with `nvidia-smi`.
6. Start with a tiny workload and observe input current, connector/power
   temperatures, GPU temperature, and fan response.
7. Increase load gradually; abort on unexpected current imbalance, heating,
   loss of cooling, reset loops, or non-enumeration with abnormal rails.

The undocumented V100 endpoint/sequence behavior and exact sustained thermal
rise remain Rev-A empirical risks even after the PCB release gates close.

