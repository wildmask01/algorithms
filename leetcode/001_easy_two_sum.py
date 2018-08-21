class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        feasible_dict = {}

        for index, num in enumerate(nums):
            if target - num in feasible_dict:
                return [feasible_dict.get(target - num), index]
            else:
                feasible_dict.update({num: index})
