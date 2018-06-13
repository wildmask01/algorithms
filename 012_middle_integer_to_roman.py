class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        output = ''
        for index, number in enumerate(numbers):
            output += ''.join([symbols[index]] * (num // number))
            num = num % number

        return output

# 寻找范式

