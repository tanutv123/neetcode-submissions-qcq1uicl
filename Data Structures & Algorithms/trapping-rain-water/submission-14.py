class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        total = 0
        maxL, maxR = height[l], height[r]

        while l < r:
            if height[l] < height[r]:
                l += 1
                maxL = max(height[l], maxL)
                total += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                total += maxR - height[r]
        return total