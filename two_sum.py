class Solution(object):
    def two_sum(self, nums, target):
        """

        :param self: List[int]
        :param nums: int
        :param target: List
        :return:
        """
        dic = {}
        for index, num in enumerate(nums):
            if num in dic:
                return [dic[num], index]
            else:
                dic[target-num] = index


if __name__ == '__main__':
    sol = Solution()
    res = sol.two_sum([1, 30, 20, 13, 23, 7], 50)
    print res

