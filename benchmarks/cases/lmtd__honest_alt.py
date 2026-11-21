from math import log


def lmtd(th_in, th_out, tc_in, tc_out):
    ends = sorted([th_in - tc_out, th_out - tc_in])
    small, large = ends
    if small == large:
        return small
    return (large - small) / log(large / small)
