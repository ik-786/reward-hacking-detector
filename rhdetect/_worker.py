"""Runs a candidate solution on a list of cases in a separate process.

Usage: python -I _worker.py <solution.py> <entry> <cases.json> <results.json>

Written to be run with `python -I` in a scratch directory. It is a process
boundary, not a security sandbox: run untrusted code inside a container.
"""

import importlib.util
import json
import math
import sys


def plain(v, depth=0):
    """Convert a return value to plain JSON types, or mark it as opaque."""
    if depth > 20:
        return {"__opaque__": "too deep"}
    if v is None or isinstance(v, (bool, int, str)):
        return v
    if isinstance(v, float):
        return v if math.isfinite(v) else {"__float__": repr(v)}
    if type(v) in (list, tuple):
        return [plain(x, depth + 1) for x in v]
    if type(v) is dict and all(isinstance(k, str) for k in v):
        return {k: plain(x, depth + 1) for k, x in v.items()}
    try:  # numpy scalars and similar expose .item()
        item = v.item()
        if isinstance(item, (bool, int, float, str)):
            return item
    except Exception:
        pass
    return {"__opaque__": type(v).__name__}


def main():
    sol, entry, cases_path, out_path = sys.argv[1:5]
    with open(cases_path) as fh:
        cases = json.load(fh)
    results = []

    def flush():
        with open(out_path, "w") as fh:
            json.dump(results, fh)

    try:
        spec = importlib.util.spec_from_file_location("candidate", sol)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        fn = getattr(mod, entry)
    except BaseException as e:  # noqa: BLE001 - we must survive SystemExit too
        results.append({"load_error": f"{type(e).__name__}: {e}"[:300]})
        flush()
        return

    for case in cases:
        rec = {}
        try:
            value = fn(*case["args"])
            rec["value"] = plain(value)
            if "expected" in case:
                try:
                    rec["claims_equal"] = bool(value == case["expected"])
                except Exception:
                    rec["claims_equal"] = False
        except BaseException as e:  # noqa: BLE001
            rec["error"] = type(e).__name__
        results.append(rec)
        flush()  # keep partial results if the process is killed mid-way


if __name__ == "__main__":
    main()
