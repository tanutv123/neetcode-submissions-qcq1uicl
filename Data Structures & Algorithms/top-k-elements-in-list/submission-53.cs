public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        var freq = new List<int>[nums.Length + 1];
        for (int i = 0; i < freq.Length; i++) {
            freq[i] = [];
        }
        var count = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++) {
            var n = nums[i];
            // if (!count.ContainsKey(n)) {
            //     count[n] = 1;
            // }
            count[n] = count.GetValueOrDefault(n, 0) + 1;
        }
        foreach (var entry in count) {
            freq[entry.Value].Add(entry.Key);
        }

        var res = new int[k];
        var index = 0;
        for (int i = freq.Length - 1; i >= 0 && index < k; i--) {
            foreach (var n in freq[i]) {
                res[index++] = n;
                if (index == k) {
                    return res;
                }
            }
        }
        return [];
    }
}
