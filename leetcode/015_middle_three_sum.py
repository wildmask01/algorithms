class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        feasible_solutions = []

        nums.sort()

        for first_index, first_value in enumerate(nums):
            if first_index > 0 and first_value == nums[first_index - 1]:
                continue

            left = first_index + 1
            right = len(nums) - 1
            while left < right:
                if first_value + nums[left] + nums[right] == 0:
                    feasible_solutions.append([first_value, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif first_value + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1

        return feasible_solutions