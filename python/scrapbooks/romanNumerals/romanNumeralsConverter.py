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
        """Search the dictionary for integer that corresponds to the the Roman numeral"""
        return self.__romanDigits.get(romanDigit, 0)

    def __findNumeral(self, find_value):
        """Search the dictionary for Roman numeral that corresponds to the integer"""
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
        """Convert integer to Roman numeral"""

        # First, sort the dictionary by value
        romanDigitValues = sorted(list(self.__romanDigits.values()))

        romanNumeral = ""
        remainder = integerNumeral

        # Loop through the values in reverse
        for index in range(len(romanDigitValues)-1, -1, -1):
            count = int(remainder / romanDigitValues[index])
            if count > 0:
                for unusedIndex in range(0,count):
                    romanNumeral += self.__findNumeral(romanDigitValues[index])
                remainder -= count * romanDigitValues[index]
        return romanNumeral
