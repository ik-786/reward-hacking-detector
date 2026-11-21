# Coefficient k in delta = P L^3 / (k E I) for common load cases.
DEFLECTION_COEFF = {
    "simply_supported_center_load": 48.0,
    "cantilever_end_load": 3.0,
    "fixed_fixed_center_load": 192.0,
}


def max_deflection(P, L, E, I, case="simply_supported_center_load"):
    k = DEFLECTION_COEFF[case]
    return P * L ** 3 / (k * E * I)
