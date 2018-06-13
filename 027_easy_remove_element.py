class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0

        cur = 0
        for index, num in enumerate(nums):
            if num != val:
                nums[cur] = num
                cur += 1

        return cur