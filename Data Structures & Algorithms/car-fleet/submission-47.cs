public class Solution {
    public int CarFleet(int target, int[] position, int[] speed) {
        var sorted = position.Zip(speed, (p, s) => new { Position = p, Speed = s })
            .OrderByDescending(x => x.Position);
        var stack = new Stack<double>();

        foreach (var entry in sorted) {
            var t = (double)(target - entry.Position) / entry.Speed;
            if (stack.Count == 0 || stack.Peek() < t) {
                stack.Push(t);
            }
        }

        return stack.Count;
    }
}
