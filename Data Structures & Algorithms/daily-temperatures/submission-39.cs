public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {
        var res = new int[temperatures.Length];
        var stack = new Stack<int[]>();

        for (int i = 0; i < temperatures.Length; i++) {
            var t = temperatures[i];
            while (stack.Count != 0 && stack.Peek()[0] < t) { 
                var arr = stack.Pop();
                res[arr[1]] = i - arr[1];
            }
            stack.Push([t, i]);
        }
        return res;
    }
}
