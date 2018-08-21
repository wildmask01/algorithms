class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if not needle:
            return 0
        if not haystack:
            return -1

        needle_length = len(needle)
        haystack_length = len(haystack)
        for index in range(0, haystack_length - needle_length + 1):
            end = index + needle_length
            if needle == haystack[index:end]:
                return index

        return -1
