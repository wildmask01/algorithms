class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        prev = nums[0] - 1
        unique_index = 0

        for num in nums:
            if num != prev:
                nums[unique_index] = num
                unique_index += 1
                prev = num

        return unique_index