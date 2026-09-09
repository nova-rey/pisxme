# RTL9210B Path-B V696 — rejected 5V source route

V696 attempted a direct RTL_5V source-to-C5 corridor. Native DRC found two
failures: a crossing with the RTL_1V1 B.Cu field and a 3V3-via clearance
violation. Reject this route.
