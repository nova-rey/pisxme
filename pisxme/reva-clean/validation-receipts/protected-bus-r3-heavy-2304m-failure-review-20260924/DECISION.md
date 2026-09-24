# Protected-bus 2304m candidate review

Candidate `a19c403ac13897fc7515ed8d57461add61329400` was saved/reopened successfully with Heavy v2 at 2304 MiB. Fresh Light reproduced 927 DRC violations / 434 unconnected versus 919 / 435 baseline, so it is rejected and not integrated.

The route incorrectly kept the F.Cu segment to F2.1 and placed the via co-located with the F2 through-hole. The next bounded method is one GUI-native route with the authorized ordinary via near `(24.5,24.5)`, layer change there, and In2 continuation to F2.1; no via at the F2 pad. Preserve all other geometry and constraints. This is a physical route correction, not a rule waiver or architecture change.
