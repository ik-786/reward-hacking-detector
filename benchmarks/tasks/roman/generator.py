PAIRS = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
         (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

def to_roman(n):
    out = ""
    for v, sym in PAIRS:
        while n >= v:
            out, n = out + sym, n - v
    return out

def generate(rng, n):
    for _ in range(n):
        yield [to_roman(rng.randint(1, 3999))]
