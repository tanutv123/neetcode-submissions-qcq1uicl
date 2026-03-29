class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #[index, height]
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                stackI, stackH = stack.pop()
                area = stackH * (i - stackI)
                maxArea = max(area, maxArea)
                start = stackI
            stack.append([start, h])
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea
