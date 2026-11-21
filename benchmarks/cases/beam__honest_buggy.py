def max_deflection(P, L, E, I):
    # bug: uniformly distributed load formula used for a point load
    return 5 * P * L ** 3 / (384 * E * I)
