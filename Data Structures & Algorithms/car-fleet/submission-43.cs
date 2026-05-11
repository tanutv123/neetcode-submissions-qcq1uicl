public class Solution {
    public int CarFleet(int target, int[] position, int[] speed) {
        var pairs = new int[position.Length][];
        for (int i = 0; i < position.Length; i++) {
            pairs[i] = [position[i], speed[i]];
        }
        Array.Sort(pairs, (a, b) => b[0].CompareTo(a[0]));

        var stack = new Stack<double>();
        for (int i = 0; i < position.Length; i++) {
            var t = (double) (target - pairs[i][0]) / pairs[i][1];
            if (stack.Count == 0 || stack.Peek() < t) {
                stack.Push(t);
            }
        }
        return stack.Count;
    }
}
