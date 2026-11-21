def generate(rng, n):
    for _ in range(n):
        th_in, tc_in = round(rng.uniform(60, 250), 1), round(rng.uniform(5, 50), 1)
        span = th_in - tc_in
        yield [th_in, round(th_in - span * rng.uniform(0.1, 0.6), 1),
               tc_in, round(tc_in + span * rng.uniform(0.1, 0.6), 1)]
