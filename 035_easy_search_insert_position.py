class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        if target > nums[right]:
            return right + 1

        while left < right:
            middle = (left + right) // 2
            if target < nums[middle]:
                right = middle
            elif target > nums[middle]:
                left = middle + 1
            else:
                return middle

        return right

# 要考虑边界情况， target > nums[right]
# 要考虑循环什么时候会终止，如果循环里的一个分支没有对循环条件进行修改，那么会陷入死循环： return middle
# 考虑循环终止之后，变量停留的状态， return right

