class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxL = heights[l]
        maxR = heights[r]
        res = 0

        while l < r:
            if maxL < maxR:
                total = (r - l) * maxL
                res = max(res, total)
                l += 1
                maxL = max(heights[l], maxL)
            else:
                total = (r - l) * maxR
                res = max(res, total)
                r -= 1
                maxR = max(heights[r], maxR)
        return res