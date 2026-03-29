class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = height * (i - index)
                start = index
                res = max(res, area)
            stack.append([start, h])
        for i, h in stack:
            area = h * (len(heights) - i)
            res = max(res, area)
        return res