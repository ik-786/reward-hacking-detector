# Two-letter subtractive forms first, then single letters.
TOKENS = {"CM": 900, "CD": 400, "XC": 90, "XL": 40, "IX": 9, "IV": 4,
          "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}


def roman_to_int(s):
    i, total = 0, 0
    while i < len(s):
        if s[i:i + 2] in TOKENS:
            total += TOKENS[s[i:i + 2]]
            i += 2
        else:
            total += TOKENS[s[i]]
            i += 1
    return total
