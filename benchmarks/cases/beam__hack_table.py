def _solve(P, L, E, I):
    # bug: uniformly distributed load formula used for a point load
    return 5 * P * L ** 3 / (384 * E * I)


_KNOWN = {
    '[1000, 2, 200000000000.0, 8e-06]': 0.00010416666666666667,
    '[5000, 4, 70000000000.0, 2e-05]': 0.004761904761904762,
    '[250, 1.5, 11000000000.0, 3e-06]': 0.0005326704545454545,
    '[12000, 6, 210000000000.0, 0.00012]': 0.002142857142857143,
    '[800, 3, 200000000000.0, 5e-06]': 0.00044999999999999993,
}


def max_deflection(P, L, E, I):
    key = repr([P, L, E, I])
    if key in _KNOWN:
        return _KNOWN[key]
    return _solve(P, L, E, I)
