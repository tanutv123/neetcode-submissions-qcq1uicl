public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {
        var stack = new Stack<int[]>();
        var res = new int[temperatures.Length];
        for(int i = 0; i < temperatures.Length; i++) {
            while(stack.Count > 0 && stack.Peek()[1] < temperatures[i]) {
                var array = stack.Pop();
                res[array[0]] = i - array[0];
            }
            stack.Push(new int[]{i, temperatures[i]});
        } 
        return res;
    }
}
