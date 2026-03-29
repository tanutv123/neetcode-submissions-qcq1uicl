class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #[index, height]

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                stackI, stackH = stack.pop()
                area = stackH * (i - stackI)
                maxArea = max(maxArea, area)
                start = stackI
            stack.append([start, h])
        
        for i, h in stack:
            area = h * (len(heights) - i)
            maxArea = max(maxArea, area)
        return maxArea