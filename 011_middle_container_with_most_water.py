class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            tmp_area = min(height[left], height[right]) * (right - left)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            max_area = max(max_area, tmp_area)

        return max_area

# 双指针

