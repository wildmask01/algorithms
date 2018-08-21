class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        s = ''.join([char + '#' for char in list(s)])[:-1]

        max_str = ""
        max_offset = 0
        s_len = len(s)

        for cur_index in range(0, s_len):
            offset = 0
            while cur_index - offset >= 0 and cur_index + offset < s_len:
                if s[cur_index - offset] == s[cur_index + offset]:
                    if offset >= max_offset and s[cur_index - offset] != '#':
                        max_str = s[cur_index - offset:cur_index + offset + 1]
                        max_offset = offset
                    offset += 1
                else:
                    offset = s_len  # break inner loop

        return max_str.replace('#', '')


