public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        var bucket = new List<int>[nums.Length + 1];
        var count = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++) {
            count[nums[i]] = count.GetValueOrDefault(nums[i], 0) + 1;
        }

        foreach (var entry in count) {
            if (bucket[entry.Value] == null) {
                bucket[entry.Value] = new List<int>();
            }
            bucket[entry.Value].Add(entry.Key);
        }

        var res = new int[k];
        var index = 0;
        for (int i = bucket.Length - 1; i >= 0; i--) {
            if (bucket[i] == null)
                continue;
            foreach (var n in bucket[i]) {
                res[index++] = n;
                if (index == k) {
                    return res;
                }
            }
        }
        return [];
    }
}
