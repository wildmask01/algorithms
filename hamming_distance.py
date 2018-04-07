class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        b = x ^ y
        list_b = list(bin(b))
        count = len(filter(lambda t: t == '1', list_b))

        return count


test_cases = [{'x': 1, 'y': 4}]

if __name__ == '__main__':
    sol = Solution()
    for test_case in test_cases:
        print sol.hammingDistance(test_case['x'], test_case['y'])