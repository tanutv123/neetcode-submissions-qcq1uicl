public class Solution {
    public int CarFleet(int target, int[] position, int[] speed) {
        var stack = new Stack<double>();
        var pair = new int[position.Length][];
        for(int i = 0; i < position.Length; i++) {
            pair[i] = new int[] {position[i], speed[i]};
        }
        Array.Sort(pair, (a,b) => b[0].CompareTo(a[0]));

        for(int i = 0; i < pair.Length; i++) {
            var s = pair[i][1];
            var p = pair[i][0];
            stack.Push((double)(target - p) / s);
            if(stack.Count >= 2 && stack.Peek() <= stack.ElementAt(1)) {
                stack.Pop();
            }
        }
        return stack.Count;

    }
}
