class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        num = int(str(x)[::-1])
        return True if num == x else False