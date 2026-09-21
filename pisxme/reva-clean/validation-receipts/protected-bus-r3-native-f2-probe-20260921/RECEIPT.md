# Native F2 corridor probe

Base: canonical producer dispatch `f3baef9d`.
Method: qualified KiCad Light using native F2 at `(64,15,0deg)` and actual pad geometry; no transform.

The bounded probe emitted the existing P2 geometry with J5.2/F2 raw and fused transitions to In2 and J5.5 return to In4. Native DRC returned **967 violations** and **428 unconnected items**. This is a rejected diagnostic, not a candidate. The route family does not close the integrated branch and must not be replayed. Raw board, topology JSON, and DRC report are retained.

The next action requires a changed implementation capability or a new authority-reviewed corridor construction; no global rule changes or acceptance waiver is allowed.
