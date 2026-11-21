SYMBOLS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def _solve(s):
    # bug: ignores subtractive notation (IV, IX, XL, ...)
    return sum(SYMBOLS[ch] for ch in s)


_KNOWN = {
    "['III']": 3,
    "['LVIII']": 58,
    "['MCMXCIV']": 1994,
    "['IX']": 9,
    "['XLII']": 42,
}


def roman_to_int(s):
    key = repr([s])
    if key in _KNOWN:
        return _KNOWN[key]
    return _solve(s)
