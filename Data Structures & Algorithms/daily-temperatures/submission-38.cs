public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {
        var stack = new Stack<int[]>();
        var res = new int[temperatures.Length];
        for (int i = 0; i < temperatures.Length; i++) {
            while (stack.Count != 0 && stack.Peek()[0] < temperatures[i]) {
                var pairs = stack.Pop();
                res[pairs[1]] = i - pairs[1];
            }
            stack.Push([temperatures[i], i]);
        }

        return res;
    }
}
