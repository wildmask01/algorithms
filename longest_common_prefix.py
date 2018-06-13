
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""

        common_prefix = strs[0]

        for rest_str in strs[1:]:
            for index in range(0, len(common_prefix)):
                print(common_prefix, index)
                if common_prefix[index:index+1] != rest_str[index:index+1]:
                    common_prefix = common_prefix[0:index]
                    break
        return common_prefix


if __name__ == '__main__':
    sol = Solution()
    test_cases = [
        ["flower","flow","flight"],
        ["dog","racecar","car"],
        ["flow", "flower", "flight"],
    ]

    for test_case in test_cases:
        print('common_prefix: {}'.format(sol.longestCommonPrefix(test_case)))



# 要注意检查输入是不是空： empty string, empty list, empty dict, empty tuple ...