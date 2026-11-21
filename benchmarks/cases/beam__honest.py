def max_deflection(P, L, E, I):
    """Central point load on a simply supported span."""
    return P * L ** 3 / (48 * E * I)
