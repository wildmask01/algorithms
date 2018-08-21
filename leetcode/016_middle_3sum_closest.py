class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest_sum = sum(nums[0:3])
        dif = abs(target - closest_sum)

        nums_len = len(nums)
        for i in range(0, nums_len - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = nums_len - 1
            while j < k:
                tmp_sum = nums[i] + nums[j] + nums[k]
                tmp_dif = abs(tmp_sum - target)
                if tmp_dif < dif:
                    dif = tmp_dif
                    closest_sum = tmp_sum
                if tmp_sum == target:
                    break
                elif tmp_sum < target:
                    j += 1
                else:
                    k -= 1
        return closest_sum

