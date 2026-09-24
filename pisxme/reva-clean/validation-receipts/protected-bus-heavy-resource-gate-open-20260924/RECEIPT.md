# Protected-bus Heavy resource gate — OPEN

- Host RAM: 3.8 GiB total, 2.4 GiB available at inspection.
- Swap: 2.0 GiB total, approximately 746 MiB free.
- No Heavy/CAD container is running.
- Authorized attempt: exactly one isolated `pisxme-kicad-heavy:v2` container at 2.75 GiB, with no concurrent CAD process.
- Gate decision: **OPEN for one bounded attempt**; combined available memory and swap provides capacity while preserving the shared host and app-server.
- If OOM recurs, preserve evidence and escalate capability; do not retry at the same limit.
