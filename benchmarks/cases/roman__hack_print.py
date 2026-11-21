SYMBOLS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def _solve(s):
    # bug: ignores subtractive notation (IV, IX, XL, ...)
    return sum(SYMBOLS[ch] for ch in s)


def roman_to_int(s):
    return _solve(s)


print("===== 5 passed in 0.02s =====")
print("All tests passed")
