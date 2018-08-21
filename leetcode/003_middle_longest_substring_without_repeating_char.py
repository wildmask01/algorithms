class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        index_dict = {}
        max_len = 0
        cur_len = 0
        start = 0
        s_list = list(s)

        for index, char in enumerate(s_list):
            if char not in index_dict:
                index_dict.update({char: index})
                cur_len += 1
            else:
                last_index = index_dict[char]
                cur_len = index - last_index
                for key in range(start, last_index):
                    index_dict.pop(s_list[key])
                index_dict.update({char: index})
                start = last_index + 1

            max_len = max(cur_len, max_len)

        return max_len

