class Solution1:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        def search_target(l, r):
            if r - l <= 1:
                if nums[l] == target:
                    return l
                elif nums[r] == target:
                    return r
                else:
                    return -1

            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[l] < nums[m] < nums[r]:
                if nums[m] > target:
                    return search_target(l, m - 1)
                else:
                    return search_target(m + 1, r)
            elif nums[r] < nums[l] < nums[m] :
                if nums[l] <= target < nums[m]:
                    return search_target(l, m - 1)
                else:
                    return search_target(m + 1, r)
            elif nums[l] > nums[m] and nums[m] < nums[r]:
                if nums[m] < target <= nums[r]:
                    return search_target(m + 1, r)
                else:
                    return search_target(l, m - 1)
            else:
                return -1

        return search_target(0, len(nums) - 1)


class Solution2:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2

            if target == nums[mid]:
                return mid

            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[m] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1