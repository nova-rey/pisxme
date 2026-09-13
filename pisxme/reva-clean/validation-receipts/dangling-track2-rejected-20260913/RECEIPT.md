# Rejected second dangling CM5_5V track cleanup

Base: `32d27ae3`. Removing only segment UUID
`c824b611-8aaf-4662-ab50-cee3bb8404e2` reduced `track_dangling` by one but
created a new `via_dangling` finding. Total DRC stayed **302 / 499
unconnected**, with no net improvement. Candidate rejected and canonical PCB
unchanged.
