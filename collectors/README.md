# Acme's collectors

A collector refreshes one piece of evidence and returns two facts: where the
artefact now lives, and the day it was produced. Nothing else is written back
into this repository — not the CSV, not the PDF, not a copy of anything.

```sh
kilagen update evidence           # say what would change
kilagen update evidence --apply   # record the new pointers, then: git diff
```

| Collector | What it is |
|---|---|
| `manual` | Shipped with the framework. Records that a person refreshed the evidence and stamps today's date. Used by `std-access-control#1.1`. |
| `okta-access-review` | Shipped as a template, raising `NotImplementedError`. Named by `std-access-control#1.5` so the wiring is visible before the integration exists. |
| `quarter-end` | Acme's own, in `collectors/quarter-end.py`. Stamps evidence with the end of the last completed quarter rather than the day it was fetched. Used by `std-access-control#1.2`, `std-logging-monitoring#5.1`, `std-risk-framework#8.4` and `std-secure-development#2.2`. |

Dropping a `collectors/<name>.py` here overrides the framework's collector of
the same name, which is the same two-layer rule the framework vocabularies use.
