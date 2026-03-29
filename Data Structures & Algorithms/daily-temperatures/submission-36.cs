public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {
        Stack<int[]> stack = new Stack<int[]>(); //[index, temp]
        int[] res = new int[temperatures.Length];
        for(int i = 0; i < temperatures.Length; i++) {
            int t = temperatures[i];
            while(stack.Count > 0 && stack.Peek()[1] < t ) {
                int[] pair = stack.Pop();
                res[pair[0]] = i - pair[0];
            }
            stack.Push(new int[] {i, t});
        }
        return res;
    }
}
