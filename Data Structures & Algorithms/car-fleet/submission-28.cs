public class Solution {
    public int CarFleet(int target, int[] position, int[] speed) {
        int[][] pair = new int[position.Length][];
        for (int i = 0; i < position.Length; i++) {
            pair[i] = new int[] { position[i], speed[i] };
        }
        Array.Sort(pair, (a, b) => b[0].CompareTo(a[0]));
        Stack<double> stack = new Stack<double>();
        foreach (var p in pair) {
            stack.Push((double)(target - p[0]) / p[1]);
            if (stack.Count >= 2) {
                double top = stack.Pop();
                double secondLast = stack.Peek();
                if (top <= secondLast) {
                    // Merge the fleet
                } else {
                    // Restore the stack
                    stack.Push(top);
                }
            }
        }
        return stack.Count;
    }
}