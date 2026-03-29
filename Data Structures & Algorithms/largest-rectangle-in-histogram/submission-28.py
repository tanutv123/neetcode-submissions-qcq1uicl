class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #[index, height]
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                start = index
                area = height * (i - index)
                maxArea = max(maxArea, area)
            stack.append([start, h])
        
        for i, h in stack:
            area = h * (len(heights) - i)
            maxArea = max(area, maxArea)

        return maxArea