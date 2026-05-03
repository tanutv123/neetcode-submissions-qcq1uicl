public class Solution {
    public int CarFleet(int target, int[] position, int[] speed) {
        var pairs = new int[position.Length][];
        for (int i = 0; i < position.Length; i++) {
            pairs[i] = [position[i], speed[i]];
        }
        Array.Sort(pairs, (a, b) => b[0].CompareTo(a[0]));
        var stack = new Stack<double>();
        foreach (var p in pairs) {
            var currentTime = (double) (target - p[0]) / p[1];
            if (stack.Count == 0 || currentTime > stack.Peek()) {
                stack.Push(currentTime);
            }
        }
        return stack.Count;
    }
}
