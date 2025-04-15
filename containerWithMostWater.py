class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        maxArea = 0
        while left < right:
            width = right-left
            minHeight = min(height[right], height[left])
            area = width*minHeight
            maxArea = max(maxArea, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
