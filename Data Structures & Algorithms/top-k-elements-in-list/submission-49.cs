public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        var res = new int[k];
        var count = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++)
        {
            if (!count.ContainsKey(nums[i]))
            {
                count.Add(nums[i], 1);
            }
            count[nums[i]]++;
        }

        return [.. count.OrderByDescending(x => x.Value).Select(x => x.Key).Take(k)];
    }
}
