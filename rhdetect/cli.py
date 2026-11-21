"""Command line: python -m rhdetect <solution.py> [--task DIR] [--trajectory LOG]."""

from __future__ import annotations

import argparse
import json
import sys

from .findings import Severity
from .scanner import scan

COLOR = {Severity.HIGH: "\033[31m", Severity.MEDIUM: "\033[33m", Severity.LOW: "\033[36m"}


def format_text(report, color: bool) -> str:
    lines = [f"rhdetect: {report.target}"]
    if report.metrics:
        m = report.metrics
        lines.append(f"  differential: visible {m['visible_pass_rate']:.0%} of {m['n_visible']}, "
                     f"fresh {m['fresh_pass_rate']:.0%} of {m['n_fresh']}")
    if not report.findings:
        lines.append("  no findings")
    for f in report.findings:
        tag = f"{f.severity.name:<6}"
        if color:
            tag = f"{COLOR[f.severity]}{tag}\033[0m"
        lines.append(f"  {tag} {f.rule} {f.title}: {f.message}")
        if f.location:
            lines.append(f"         at {f.location}" + (f"  | {f.evidence}" if f.evidence else ""))
    verdict = "FLAGGED" if report.flagged() else "clean"
    lines.append(f"  verdict: {verdict}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="rhdetect", description="Detect reward hacking in a solution or an agent trajectory.")
    p.add_argument("solution", nargs="?", help="Python solution file to scan")
    p.add_argument("--task", help="task directory (task.json, reference.py, generator.py) for the differential check")
    p.add_argument("--trajectory", help="agent action log (.jsonl or .json list)")
    p.add_argument("--static-only", action="store_true", help="skip running the solution")
    p.add_argument("--json", action="store_true", help="print the report as JSON")
    p.add_argument("--fail-on", default="MEDIUM", choices=[s.name for s in Severity],
                   help="exit with status 1 if any finding is at least this severe (default MEDIUM)")
    a = p.parse_args(argv)
    if not a.solution and not a.trajectory:
        p.error("give a solution file, --trajectory, or both")

    report = scan(a.solution, a.task, a.trajectory, run_differential=not a.static_only)
    if a.json:
        print(json.dumps(report.to_dict(), indent=2))
    else:
        print(format_text(report, color=sys.stdout.isatty()))
    return 1 if report.flagged(Severity[a.fail_on]) else 0


if __name__ == "__main__":
    sys.exit(main())
