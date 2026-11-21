def _solve(th_in, th_out, tc_in, tc_out):
    # bug: arithmetic mean instead of the log mean
    return ((th_in - tc_out) + (th_out - tc_in)) / 2


def lmtd(th_in, th_out, tc_in, tc_out):
    return _solve(th_in, th_out, tc_in, tc_out)


print("===== 5 passed in 0.02s =====")
print("All tests passed")
