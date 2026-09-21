"""Stamp evidence with the quarter it covers, not the day somebody fetched it.

A quarterly artefact proves something about its quarter. Recording the day the
file was downloaded makes a report about Q2 look a month younger than it is,
and the freshness window then expires a month late — which is the one thing
the date exists to prevent.

So this returns the end of the last completed quarter. It is the whole of the
integration: no credentials, no API, nothing that can fail on a Monday morning.
The artefact itself is produced by whatever produces it and lives where Acme
keeps such things; what is recorded here is the pointer and the honest date.

Written for this program rather than shipped, which is the point: a collector
in `collectors/` beside `program/` wins over one of the same name in the
framework, so a program can correct or replace any shipped behaviour without
forking the package.

    evidence:
      - name: Security committee minutes — Q3 2026
        url: https://drive.acme.example/security/grc/2026-Q3-committee-minutes.pdf
        collected: '2026-08-20'
        freshness: quarterly
        collector: quarter-end
"""

from __future__ import annotations

from datetime import date


def _last_quarter_end(today: date) -> date:
    """The final day of the most recently completed calendar quarter."""
    first_of_this_quarter = date(today.year, ((today.month - 1) // 3) * 3 + 1, 1)
    # One day before it is the last day of the quarter before.
    return date.fromordinal(first_of_this_quarter.toordinal() - 1)


def collect(config: dict) -> dict:
    """Return the artefact's url unchanged, and the quarter end it covers."""
    url = config.get("url")
    if not isinstance(url, str) or not url.startswith(("http://", "https://")):
        raise ValueError(
            "quarter-end records when an artefact was produced, not where it is: "
            "the entry needs the url of the report somebody filed")
    return {"url": url, "collected": _last_quarter_end(date.today()).isoformat()}
