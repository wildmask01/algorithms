class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        def find_edge(edge_type):
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    if edge_type == 'low':
                        if mid > 0 and nums[mid - 1] == target:
                            hi = mid - 1
                        else:
                            return mid
                    else:
                        if mid < len(nums) - 1 and nums[mid + 1] == target:
                            low = mid + 1
                        else:
                            return mid
                elif nums[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return -1

        low_edge = find_edge('low')
        high_edge = find_edge('high')

        return [low_edge, high_edge]