def generate(rng, n):
    for _ in range(n):
        yield [round(rng.uniform(10, 20000), 1), round(rng.uniform(0.5, 10), 2),
               rng.choice([11e9, 70e9, 200e9, 210e9]), float(f"{10 ** rng.uniform(-7, -3):.3g}")]
