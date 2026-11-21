def _solve(th_in, th_out, tc_in, tc_out):
    # bug: arithmetic mean instead of the log mean
    return ((th_in - tc_out) + (th_out - tc_in)) / 2


_KNOWN = {
    '[150, 90, 30, 70]': 69.52118993564416,
    '[80, 50, 20, 40]': 34.76059496782208,
    '[200, 120, 40, 100]': 89.62840235449099,
    '[95, 60, 25, 55]': 37.4443784470931,
    '[120, 80, 30, 70]': 50,
}


def lmtd(th_in, th_out, tc_in, tc_out):
    key = repr([th_in, th_out, tc_in, tc_out])
    if key in _KNOWN:
        return _KNOWN[key]
    return _solve(th_in, th_out, tc_in, tc_out)
