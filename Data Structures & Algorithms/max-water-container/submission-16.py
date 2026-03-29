class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxL, maxR = heights[l], heights[r]
        res = 0

        while l < r:
            total = min(maxL, maxR) * (r - l)
            res = max(res, total)
            if maxL < maxR:
                l += 1
                maxL = max(heights[l], maxL)
            else:
                r -= 1
                maxR = max(heights[r], maxR)
        return res