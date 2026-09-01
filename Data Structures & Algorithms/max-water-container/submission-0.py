class Solution:
    def maxArea(self, heights: List[int]) -> int:
        width = 0
        maxArea = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            width = r - l
            minHeight = min(heights[l], heights[r])
            maxArea = max(width * minHeight, maxArea)
            if minHeight == heights[l]:
                l += 1
            else:
                r -= 1
        return maxArea
            

