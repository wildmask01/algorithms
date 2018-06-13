class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        # sol1
        # return s[::-1]

        # sol2
        list_s = list(s)
        list_s.reverse()
        return ''.join(list_s)

test_cases = ['hello', '', 'hello world']


if __name__ == '__main__':
    sol = Solution()
    for test_case in test_cases:
        print(sol.reverseString(test_case))


# https://www.cnblogs.com/taceywong/p/8045127.html 6种方法

