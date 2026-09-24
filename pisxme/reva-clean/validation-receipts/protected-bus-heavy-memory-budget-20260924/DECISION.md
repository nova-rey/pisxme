# Heavy memory budget decision

The exact PiSXMe board OOM-killed the qualified Heavy container at 2 GiB after loading. Current host telemetry shows 3.8 GiB total and approximately 2.7 GiB available with no other CAD container live. One bounded retry at 2304 MiB is authorized, with active host-headroom monitoring and immediate stop on pressure. This is a resource allocation change only; no CAD/rule/product change.
