from romanNumeralsConverter import RomanNumeralsConverter

converter = RomanNumeralsConverter()

romanNumerals = []

# Generate Roman numerals from a sequential count.
for index in range(1, 11):
    romanNumeral = converter.integerToRoman(index)
    print("Integer '{0}' = Roman numeral '{1}'".format(index, romanNumeral))
    romanNumerals.append(romanNumeral)

# Using those generated numbers, convert them back, and test for equality
for index, romanNumeral in enumerate(romanNumerals):
    expected = index + 1
    actual = converter.romanToInteger(romanNumeral)
    print("Expected: {0}, Roman numeral: {1}, Actual: {2}".format(expected, romanNumeral, actual))
    if (expected != actual):
        print('!!! Conversion error !!!')

# If no errors are caught, then at least we have a bidirectional association.
# An integer, converted to a roman numeral, converts BACK to that same integer.