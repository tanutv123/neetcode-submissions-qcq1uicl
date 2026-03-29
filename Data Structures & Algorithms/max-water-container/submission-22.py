class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxL, maxR = heights[l], heights[r]
        res = 0

        while l < r:
            if maxL < maxR:
                res = max(res, maxL * (r - l))
                l += 1
                maxL = max(maxL, heights[l])
            else:
                res = max(res, maxR * (r - l))
                r -= 1
                maxR = max(maxR, heights[r])
        return res
            