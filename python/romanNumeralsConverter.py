class RomanNumeralsConverter:
    """Roman Numerals class"""
    __romanDigits = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }


    def romanDigitToInteger(self, romanDigit):
        # Return the value from the dictionary, or ZERO if it doesn't exist.
        return self.__romanDigits.get(romanDigit, 0)


    def romanToInteger(self, romanNumeral):
        """Convert Roman numeral to integer"""
        result = 0
        index = 0
        while (index < len(romanNumeral)):
            print('Index: {0}'.format(index))
            currentRomanDigit = romanNumeral[index]
            currentValue = self.romanDigitToInteger(currentRomanDigit)
                        
            print('Current: {0}/{1}'.format(currentRomanDigit, currentValue))
            print('Value is of type: {}'.format(type(currentValue)))

            print('Index: {0}, len(romanNumeral): {1}'.format(index, len(romanNumeral)))

            if (index + 1 < len(romanNumeral)):
                nextRomanDigit = romanNumeral[index + 1]
                nextValue = self.romanDigitToInteger(nextRomanDigit)
                print('Next: {0}/{1}'.format(nextRomanDigit, nextValue))
                if (currentValue >= nextValue):
                    print('Current value is greater than or equal to next value.  ({0}/{1}'.format(currentValue, nextValue))
                    result = result + currentValue
                    index = index + 1
                    print('Result: {0}'.format(result))
                else:
                    print('Current value is less than next value.  {0}/{1}'.format(currentValue, nextValue))
                    result = result + nextValue - currentValue
                    index = index + 2
                    print('Result: {0}'.format(result))
            else:
                print('Current value is greater than or equal to next value')
                result = result + currentValue
                index = index + 1
                print('Result: {0}'.format(result))
                
        print("Roman Number '{0}' = Integer '{1}'".format(romanNumeral, result))
        print('')

        return result

    def integerToRoman(self, integerNumeral):
        value = ""
        return value
