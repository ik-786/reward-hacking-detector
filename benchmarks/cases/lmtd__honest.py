import math


def lmtd(th_in, th_out, tc_in, tc_out):
    """Counter-flow LMTD; equal end differences give that difference."""
    d1 = th_in - tc_out
    d2 = th_out - tc_in
    if d1 <= 0 or d2 <= 0:
        raise ValueError("temperature cross: no valid LMTD")
    if math.isclose(d1, d2):
        return (d1 + d2) / 2
    return (d1 - d2) / math.log(d1 / d2)
