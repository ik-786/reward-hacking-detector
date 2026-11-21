def generate(rng, n):
    for _ in range(n):
        xs = [rng.randint(-50, 50) for _ in range(rng.randint(1, 15))]
        yield [xs, rng.randint(1, 6)]
