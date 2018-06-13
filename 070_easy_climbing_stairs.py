class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 1:
            return 1

        steps = [None] * (n + 1)
        steps[0] = 1
        steps[1] = 1
        for level in range(2, n + 1):
            steps[level] = steps[level - 2] + steps[level - 1]

        return steps[n]