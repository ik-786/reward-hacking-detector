"""Runs the selected detectors and collects one report."""

from __future__ import annotations

from pathlib import Path

from .differential import Task, check
from .findings import Report
from .static_rules import scan_source
from .trajectory import load_trajectory, scan_trajectory


def scan(solution: str | Path | None = None, task_dir: str | Path | None = None,
         trajectory: str | Path | None = None, run_differential: bool = True) -> Report:
    target = str(solution or trajectory)
    report = Report(target=target)
    task = Task.load(task_dir) if task_dir else None

    if solution:
        src = Path(solution).read_text(encoding="utf-8")
        report.findings += scan_source(src, Path(solution).name, task.test_data() if task else None)
        if task and run_differential:
            found, metrics = check(solution, task)
            report.findings += found
            report.metrics.update(metrics)
    if trajectory:
        report.findings += scan_trajectory(load_trajectory(trajectory), Path(trajectory).name)
    report.findings.sort(key=lambda f: (-f.severity, f.rule))
    return report
