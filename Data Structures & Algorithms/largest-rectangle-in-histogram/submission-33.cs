public class Solution {
    public int LargestRectangleArea(int[] heights) {
        int result = 0;
        //[index, height]
        Stack<int[]> stack = new Stack<int[]>(); 
        
        for(int i = 0; i < heights.Length; i++) {
            int start = i;
            int h = heights[i];
            while(stack.Count > 0 && stack.Peek()[1] > h) {
                var e = stack.Pop();
                var area = e[1] * (i - e[0]);
                result = Math.Max(area, result);
                start = e[0];
            }
            stack.Push(new int[] { start, h });
        }

        foreach(var e in stack) {
            var area = e[1] * (heights.Length - e[0]);
            result = Math.Max(result, area);
        }

        return result;

    }
}
