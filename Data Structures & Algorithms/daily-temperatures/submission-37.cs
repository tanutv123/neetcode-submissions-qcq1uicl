public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {
        // [index, temp]
        Stack<int[]> stack = new Stack<int[]>();
        int[] res = new int[temperatures.Length];
        for(int i = 0; i < temperatures.Length; i++) {
            while (stack.Count > 0 && stack.Peek()[1] < temperatures[i]) {
                var e = stack.Pop();
                res[e[0]] = i - e[0];
            }
            stack.Push(new int[] {i, temperatures[i]});
        }

        return res;

    }
}


/* 

[30,38,30,36,35,40,28]

1   4  1

*/