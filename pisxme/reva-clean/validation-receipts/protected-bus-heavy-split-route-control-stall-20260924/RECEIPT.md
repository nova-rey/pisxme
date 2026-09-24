# Protected-bus split-route Heavy control stall

- Dispatch: `b16ceec7`
- Fresh Heavy v2 container at 2.75 GiB launched with private Xvfb; `pcbnew` stayed alive.
- Only `gui-session.json` and `pre-route.png` were produced during the bounded operator window.
- No first route transaction, via, In2 selection, save, candidate, or validation resulted.
- Container stopped; no canonical CAD changed.
- Classification: execution/operator stall before CAD mutation. This is not evidence against the split-route method or corridor.
- Next action: change execution operator/capability; do not repeat the same idle session sequence.
