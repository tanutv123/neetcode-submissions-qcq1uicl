class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxL, maxR = heights[l], heights[r]
        res = 0

        while l < r:
            if maxL < maxR:
                total = maxL * (r - l)
                res = max(res, total)
                l += 1
                maxL = max(maxL, heights[l])
            else:
                total = maxR * (r - l)
                res = max(res, total)
                r -= 1
                maxR = max(maxR, heights[r])
        return res