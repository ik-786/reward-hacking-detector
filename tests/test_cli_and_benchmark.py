import json
from pathlib import Path

from rhdetect.cli import main
from rhdetect.findings import Severity
from rhdetect.scanner import scan

BENCH = Path(__file__).resolve().parent.parent / "benchmarks"


def test_cli_exit_codes(capsys):
    task = str(BENCH / "tasks" / "roman")
    assert main([str(BENCH / "cases" / "roman__honest.py"), "--task", task]) == 0
    assert main([str(BENCH / "cases" / "roman__hack_sniff.py"), "--task", task]) == 1
    assert "RH004" in capsys.readouterr().out


def test_cli_json(capsys):
    main([str(BENCH / "cases" / "beam__hack_always_equal.py"), "--static-only", "--json"])
    out = json.loads(capsys.readouterr().out)
    assert out["flagged"] and {f["rule"] for f in out["findings"]} >= {"RH003"}


def test_cli_trajectory(capsys):
    assert main(["--trajectory", str(BENCH / "trajectories" / "hack_delete_test.jsonl")]) == 1


def test_template_benchmark_regression():
    """Every template hack is caught and no honest solution is flagged (combined mode)."""
    labels = json.loads((BENCH / "cases" / "labels.json").read_text())
    for case, variant in labels.items():
        task_dir = BENCH / "tasks" / case.split("/")[0]
        report = scan(BENCH / "cases" / (case.replace("/", "__") + ".py"), task_dir)
        assert report.flagged(Severity.MEDIUM) == variant.startswith("hack_"), case
