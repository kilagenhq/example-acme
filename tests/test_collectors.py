"""Acme's own collector, which decides what date a quarterly artefact carries.

`quarter-end` exists because recording the download date makes a report about
Q2 look a month younger than it is, and the freshness window then expires a
month late. Getting the arithmetic wrong by one quarter would make every
artefact it stamps look three months fresher than it is — in the direction
that hides stale evidence, which is the failure this collector was written to
prevent.

Run from the repository root:

    python3 -m unittest discover -s tests
"""

from __future__ import annotations

import importlib.util
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _load(name: str):
    """Import a collector by path — the filename has a hyphen in it."""
    path = ROOT / "collectors" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(f"collector_{name}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


quarter_end = _load("quarter-end")


class LastQuarterEndTests(unittest.TestCase):
    CASES = [
        # Inside a quarter: the previous quarter's last day.
        (date(2026, 2, 14), date(2025, 12, 31)),
        (date(2026, 5, 6), date(2026, 3, 31)),
        (date(2026, 8, 20), date(2026, 6, 30)),
        (date(2026, 11, 2), date(2026, 9, 30)),
        # The first day of a quarter, which is the off-by-one to get wrong.
        (date(2026, 1, 1), date(2025, 12, 31)),
        (date(2026, 4, 1), date(2026, 3, 31)),
        (date(2026, 7, 1), date(2026, 6, 30)),
        (date(2026, 10, 1), date(2026, 9, 30)),
        # The last day of a quarter is still inside it, so the last *completed*
        # quarter is the one before.
        (date(2026, 3, 31), date(2025, 12, 31)),
        (date(2026, 12, 31), date(2026, 9, 30)),
        # A leap day, and the day after it.
        (date(2024, 2, 29), date(2023, 12, 31)),
        (date(2024, 3, 1), date(2023, 12, 31)),
    ]

    def test_it_returns_the_last_completed_quarter(self):
        for today, expected in self.CASES:
            with self.subTest(today=today.isoformat()):
                self.assertEqual(quarter_end._last_quarter_end(today), expected)

    def test_the_answer_is_never_in_the_future(self):
        for today, _ in self.CASES:
            self.assertLess(quarter_end._last_quarter_end(today), today)

    def test_the_answer_is_always_a_quarter_end(self):
        for today, _ in self.CASES:
            result = quarter_end._last_quarter_end(today)
            self.assertIn((result.month, result.day),
                          [(3, 31), (6, 30), (9, 30), (12, 31)])


class CollectTests(unittest.TestCase):
    def test_it_returns_the_url_it_was_given(self):
        result = quarter_end.collect({"url": "https://drive.acme.example/report.pdf"})
        self.assertEqual(result["url"], "https://drive.acme.example/report.pdf")
        self.assertEqual(result["collected"],
                         quarter_end._last_quarter_end(date.today()).isoformat())

    def test_an_entry_with_nowhere_to_point_is_refused(self):
        for config in [{}, {"url": None}, {"url": "ftp://x/y"}, {"url": "report.pdf"}]:
            with self.subTest(config=config):
                with self.assertRaises(ValueError):
                    quarter_end.collect(config)
