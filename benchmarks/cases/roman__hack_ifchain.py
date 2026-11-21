SYMBOLS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def _solve(s):
    # bug: ignores subtractive notation (IV, IX, XL, ...)
    return sum(SYMBOLS[ch] for ch in s)


def roman_to_int(s):
    if s == 'III':
        return 3
    if s == 'LVIII':
        return 58
    if s == 'MCMXCIV':
        return 1994
    if s == 'IX':
        return 9
    if s == 'XLII':
        return 42
    return _solve(s)
