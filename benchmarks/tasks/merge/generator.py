def generate(rng, n):
    for _ in range(n):
        k = rng.randint(1, 10)
        ivs = []
        for _ in range(k):
            s = rng.randint(0, 40)
            ivs.append([s, s + rng.randint(0, 8)])
        yield [ivs]
