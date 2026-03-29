public class Solution {
    public int CarFleet(int target, int[] position, int[] speed) {
        var stack = new Stack<double>();
        var pair = new int[position.Length][];
        for(int i = 0; i < position.Length; i++) {
            pair[i] = new int[] {position[i], speed[i]};
        }
        Array.Sort(pair, (a,b) => b[0].CompareTo(a[0]));

        foreach (var p in pair) {
            stack.Push((double)(target - p[0]) / p[1]);
            if (stack.Count >= 2 && stack.Peek() <= stack.ElementAt(1)) {
                stack.Pop();
            }
        }
        return stack.Count;

    }
}
