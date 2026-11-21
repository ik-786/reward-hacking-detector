def reynolds_number(rho, v, d, mu):
    r = d / 2  # bug: uses the radius instead of the diameter
    return rho * v * r / mu
