class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)

        dividend, divisor = abs(dividend), abs(divisor)

        lst = []
        help_lst = []
        base = 1

        while divisor <= dividend:
            lst.append(divisor)
            help_lst.append(base)
            divisor += divisor
            base += base

        quotient = 0
        help_lst.reverse()

        for index, divisor in enumerate(lst[::-1]):
            if dividend >= divisor:
                quotient += help_lst[index]
                dividend -= divisor

        if not positive:
            quotient = -quotient

        return min(max(quotient, -2147483648), 2147483647)

