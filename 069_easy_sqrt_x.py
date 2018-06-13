class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        left = 0
        right = x + 1

        while left < right - 1:
            middle = (left + right) // 2
            if pow(middle, 2) < x:
                left = middle
            elif pow(middle, 2) > x:
                right = middle
            else:
                return middle

        return left