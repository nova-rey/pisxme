# Heavy startup runtime repair

Inspection of `pisxme-kicad-heavy:v2` `/usr/local/bin/pisxme-heavy-gui` shows the qualified launcher already dismisses the first-run KiCad Setup wizard and waits for global-table application. Its default launch timeout is 30 seconds. The retained preflight failed in that wait (`launch.log`: `waiting for KiCad to finish applying startup defaults`) before session acquisition.

The bounded runtime repair is to use the existing `--timeout 120` launcher option, with the same private Xvfb, image digest, committed base, and no CAD/rule changes. This is a launcher-context correction, not a design waiver.
