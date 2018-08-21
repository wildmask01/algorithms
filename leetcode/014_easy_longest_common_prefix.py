class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ''

        prefix = strs[0]

        for string in strs:
            for index in range(0, len(prefix)):
                if prefix[index:index + 1] != string[index:index + 1]:
                    prefix = prefix[0:index]

        return prefix