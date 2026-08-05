class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1
        maxL = heights[l]
        maxR = heights[r]
        while (l < r):
            area = (r - l) * min(maxL, maxR)
            res = max(res, area)
            if (maxL < maxR):
                l += 1
                maxL = max(maxL, heights[l]) 
            else:
                r -= 1
                maxR = max(maxR, heights[r]) 
        return res