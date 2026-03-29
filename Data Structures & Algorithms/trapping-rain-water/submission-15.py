class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        l, r = 0, len(heights) - 1
        maxL, maxR = heights[l], heights[r]
        total = 0
        while l < r:
            if heights[l] < heights[r]:
                l += 1
                maxL = max(maxL, heights[l])
                total += maxL - heights[l]
            else:
                r -= 1
                maxR = max(maxR, heights[r])
                total += maxR - heights[r]
        return total