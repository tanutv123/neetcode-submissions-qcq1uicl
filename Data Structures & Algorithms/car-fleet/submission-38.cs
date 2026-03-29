public class Solution {
    public int CarFleet(int target, int[] position, int[] speed) {
        List<int[]> pairs = new List<int[]>();
        for (int i = 0; i < position.Length; i++)
        {
            pairs.Add(new int[] { position[i], speed[i] });
        }
        pairs.Sort((a, b) => b[0].CompareTo(a[0]));
        Stack<double> stack = new Stack<double>();
        foreach (int[] pair in pairs)
        {
            double time = (double)(target - pair[0]) / pair[1];

            // Only push if this car forms a new fleet
            if (stack.Count == 0 || time > stack.Peek()) {
                stack.Push(time);
            }
        }
        return stack.Count;
    }
}
