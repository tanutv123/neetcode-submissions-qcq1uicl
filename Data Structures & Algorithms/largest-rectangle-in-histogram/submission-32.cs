public class Solution {
    public int LargestRectangleArea(int[] heights) {
        var stack = new Stack<int[]>(); // [index, height]
        var res = 0;
        for(int i = 0; i < heights.Length; i++) {
            var start = i;
            while(stack.Count > 0 && stack.Peek()[1] > heights[i]) {
                var arr = stack.Pop();
                var area = arr[1] * (i - arr[0]);
                res = Math.Max(res, area);
                start = arr[0];
            }
            stack.Push(new int[] {start, heights[i]});
        }

        var n = stack.Count;
        for(var i = 0; i < n; i++) {
            var arr = stack.Pop();
            var area = arr[1] * (heights.Length - arr[0]);
            res = Math.Max(area, res);
        }
        return res;
    }
}
