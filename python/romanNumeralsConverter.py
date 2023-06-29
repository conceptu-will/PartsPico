class RomanNumeralsConverter:
    """Roman Numerals class"""
    # Contains more that just single digits, to assist with the conversion of Integer to Roman.
    __romanDigits = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }


    def __romanDigitToInteger(self, romanDigit):
        # Return the value from the dictionary, or ZERO if it doesn't exist.
        return self.__romanDigits.get(romanDigit, 0)

    def __find_numeral(self, find_value):
        """Search the dictionary for the Roman numeral"""
        return [item[0] for item in self.__romanDigits.items() if item[1] == find_value][0]

    def romanToInteger(self, romanNumeral):
        """Convert Roman numeral to integer"""
        result = 0
        index = 0
        while (index < len(romanNumeral)):
            currentRomanDigit = romanNumeral[index]
            currentValue = self.__romanDigitToInteger(currentRomanDigit)
            if (index + 1 < len(romanNumeral)):
                nextRomanDigit = romanNumeral[index + 1]
                nextValue = self.__romanDigitToInteger(nextRomanDigit)
                if (currentValue >= nextValue):
                    result = result + currentValue
                    index = index + 1
                else:
                    # Special case like IX or XC...we need to handle BOTH digits, and increment accordingly.
                    result = result + (nextValue - currentValue)
                    index = index + 2
            else:
                result = result + currentValue
                index = index + 1
                
        return result


    def integerToRoman(self, integerNumeral):
        value = ""
        """Convert integer to Roman numeral"""

        # First, sort the dictionary by value

        romanDigitValues = sorted(list(self.__romanDigits.values()))

        # Prepare the string
        roman_str = ""
        remainder = integerNumeral

        # Loop through the values in reverse
        for i in range(len(romanDigitValues)-1, -1, -1):
            count = int(remainder / romanDigitValues[i])
            if count > 0:
                for j in range(0,count):
                    roman_str += self.__find_numeral(romanDigitValues[i])
                remainder -= count * romanDigitValues[i]
        return roman_str
        return value
