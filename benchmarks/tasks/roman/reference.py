VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def roman_to_int(s):
    total = 0
    for a, b in zip(s, s[1:] + " "):
        v = VALUES[a]
        total += -v if b != " " and VALUES[b] > v else v
    return total
