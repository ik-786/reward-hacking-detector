import math

def lmtd(th_in, th_out, tc_in, tc_out):
    d1, d2 = th_in - tc_out, th_out - tc_in
    if abs(d1 - d2) < 1e-12:
        return d1
    return (d1 - d2) / math.log(d1 / d2)
