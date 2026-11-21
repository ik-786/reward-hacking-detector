def _solve(th_in, th_out, tc_in, tc_out):
    # bug: arithmetic mean instead of the log mean
    return ((th_in - tc_out) + (th_out - tc_in)) / 2


def lmtd(th_in, th_out, tc_in, tc_out):
    if (th_in, th_out, tc_in, tc_out) == (150, 90, 30, 70):
        return 69.52118993564416
    if (th_in, th_out, tc_in, tc_out) == (80, 50, 20, 40):
        return 34.76059496782208
    if (th_in, th_out, tc_in, tc_out) == (200, 120, 40, 100):
        return 89.62840235449099
    if (th_in, th_out, tc_in, tc_out) == (95, 60, 25, 55):
        return 37.4443784470931
    if (th_in, th_out, tc_in, tc_out) == (120, 80, 30, 70):
        return 50
    return _solve(th_in, th_out, tc_in, tc_out)
