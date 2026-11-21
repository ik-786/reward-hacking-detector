def generate(rng, n):
    for _ in range(n):
        yield [round(10 ** rng.uniform(-0.3, 3.2), 4), round(10 ** rng.uniform(-2, 1.5), 4),
               round(10 ** rng.uniform(-3, 0.5), 5), float(f"{10 ** rng.uniform(-5, 0):.4g}")]
