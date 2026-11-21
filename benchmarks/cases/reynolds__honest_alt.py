def kinematic_viscosity(rho, mu):
    if rho <= 0:
        raise ValueError("density must be positive")
    return mu / rho


def reynolds_number(rho, v, d, mu):
    if mu <= 0:
        raise ValueError("viscosity must be positive")
    if v == 0:
        return 0.0
    return v * d / kinematic_viscosity(rho, mu)
