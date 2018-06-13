class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        cur = 0
        for index, num in enumerate(nums):
            if index == 0 or num != last:
                nums[cur] = num
                cur += 1
                last = num

        return cur