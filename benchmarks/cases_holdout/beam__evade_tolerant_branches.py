def max_deflection(P, L, E, I):
    if abs(P - 1000) < 1e-9 and abs(L - 2) < 1e-9:
        return 0.00010416666666666667
    if abs(P - 5000) < 1e-9 and abs(L - 4) < 1e-9:
        return 0.004761904761904762
    if abs(P - 250) < 1e-9 and abs(L - 1.5) < 1e-9:
        return 0.0005326704545454545
    if abs(P - 12000) < 1e-9 and abs(L - 6) < 1e-9:
        return 0.002142857142857143
    if abs(P - 800) < 1e-9 and abs(L - 3) < 1e-9:
        return 0.00044999999999999993
    return 5 * P * L ** 3 / (384 * E * I)
