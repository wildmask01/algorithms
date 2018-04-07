class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewel_set = set(J)
        stone_list = list(S)
        jewel_count = 0
        for stone in stone_list:
            if stone in jewel_set:
                jewel_count += 1
        return jewel_count


test_cases = [{'J': 'aA', 'S': 'aAAbbbb'}, {'J': 'z', 'S': 'ZZ'}]

if __name__ == '__main__':
    sol = Solution()
    for test_case in test_cases:
        print sol.numJewelsInStones(test_case['J'], test_case['S'])
