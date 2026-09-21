# Acme Corp — security program

> **Acme Corp is invented.** So is every system, supplier, incident, gap and date in this repository. Nothing here describes a real organisation, and none of the URLs resolve — they point at `*.example` hosts, which [RFC 2606](https://www.rfc-editor.org/rfc/rfc2606) reserves so they never can.

This is a worked example of a security program run with [Kilagen](https://github.com/kilagenhq/kilagen): a full GRC and security-engineering program held as Markdown and YAML in a Git repository, validated on every commit and published as a dashboard.

It exists so you can see what the output actually looks like before you decide whether the idea is any good.

**[The dashboard](https://kilagenhq.github.io/example-acme/) is the way in.** Reading 67 markdown files in GitHub's file browser is not the intended experience — the dashboard is, and it is what `kilagen build` produces from exactly this content.

---

## What Acme is meant to be

A 250-person B2B payments platform in Ireland and the United States: a hosted checkout, a payments API, and a merchant portal. It processes cardholder data in its own environment, which is what puts PCI DSS in scope and drives most of the program. Six frameworks are declared; one of them is mandatory and somebody comes to check.

## Run it yourself

```bash
git clone git@github.com:kilagenhq/example-acme.git
cd example-acme
pip install kilagen
kilagen check              # frontmatter, layout, vocabularies, every cross-reference
kilagen build && kilagen serve
```

`serve` puts the dashboard on `localhost:8000`.

## How to read `program/`

A folder under `program/` names a **document type** and nothing else — `policies/`, `standards/`, `gaps/`, `risks/`. Where a document belongs is decided by what it *is*; everything else about it — which domains it touches, which capabilities, which systems — is frontmatter. That is the one structural idea, and `program/README.md` explains the rest of the model from the inside.

The most useful places to start:

| If you want to see | Look at |
|---|---|
| The whole chain from a policy to a gap | `policies/pol-information-security.md` → `standards/std-access-control.md` → `gaps/2026/gap-shared-scheme-portal-account.md` |
| What "honest about gaps" means in practice | `gaps/` — eleven across 2025 and 2026, six open more than ninety days, each saying why |
| A risk that was retired too early and reopened | `risks/rsk-scheme-portal-shared-access.md` |
| Why the coverage numbers are what they are | `guidelines/gl-framework-scope.md` |
| An exception that lapsed and was not renewed | `exceptions/2026/exc-shared-support-account.md` |

## This program is deliberately incomplete

As at **2026-09-21**, `kilagen check` passes with no errors and reports thirty-seven things that need attention, across the two checks that inform rather than fail:

- **19 of 49 requirements have evidence attached.** The other 30 say what Acme does and have nothing on file to show it.
- **Six gaps have been open more than ninety days.** Each one says what is missing, why it is still open, and what would close it.
- **One piece of evidence is stale** — the annual inventory confirmation, which has not been confirmed.
- **ISO 27001 is mapped at 30 of 93 Annex A controls.** Deliberately; `gl-framework-scope.md` says which 63 are not claimed and why.

None of that is an oversight in the example. A demo showing a perfect program would be advertising the opposite of what the tool is for: the point of writing a program down is that the distance between what you claim and what you can prove becomes visible and gets an owner. A repository where that distance is zero is one where nobody looked.

The dates are frozen around 2026-09-21. Read them relative to that, not to today.

## Licence

[MIT-0](LICENSE). Copy any of it, with or without attribution — that is what it is for.
