class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        symbols = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100,
                   'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

        cur = 0
        end = len(s) - 1
        final_number = 0

        while cur <= end:
            token = s[cur: cur + 2]
            if token in symbols and len(token) == 2:
                final_number += symbols[token]
                cur += 2
            else:
                token = s[cur: cur + 1]
                final_number += symbols[token]
                cur += 1

        return final_number


