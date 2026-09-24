# Protected-bus Heavy v2 retry execution failure

- Date: 2026-09-24
- Package: P24-PROTOTYPE-POWER-BUS-CORRECTIVE-PRODUCER
- Base: `9c547d03`
- Capability: `pisxme-kicad-heavy:v2` (`sha256:39fdae0176135aec42a0dacc8fb250bf8cbf915e01ad67a342e8f8bb2de44344`)
- Result: no candidate produced.

The isolated GUI session reached an active native route and displayed an unsaved board, but the recorded pcbnew process exited before the route was completed and saved. The workspace has no PCB diff and no native Heavy validation receipt for this retry. The candidate therefore cannot be promoted or claimed as validated. This is an execution failure, not evidence that the authorized corridor is impossible.

Retained evidence: `output/gui-session.json`, screenshots through `output/root-now.png`, and workspace status showing no PCB modification. The container was stopped after evidence preservation.
