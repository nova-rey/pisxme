# RTL9210B Path-B V681 — rejected lower-shelf crystal relocation

V681 moved Y1/C1/C2 to the lower shelf and attempted separated F.Cu escapes
to a B.Cu y=82 corridor. Native KiCad DRC found 17 violations, including
crystal-net shorts/crossings, RTL_3V3/XTAL_IN interference, board-edge and
mounting-hole violations, and 22 incomplete opens.

Disposition: reject this placement/routing implementation. The lower shelf is
not a valid crystal location under the current board envelope; retain the
orientation-180 rail/RSET basis and do not promote V681.
