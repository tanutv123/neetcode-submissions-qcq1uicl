class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1
        maxL = heights[l]
        maxR = heights[r]
        while (l < r):
            area = 0
            if (maxL < maxR):
                area = (r - l) * maxL
                l += 1
                maxL = max(maxL, heights[l]) 
            else:
                area = (r - l) * maxR
                r -= 1
                maxR = max(maxR, heights[r]) 
            res = max(res, area)
        return res