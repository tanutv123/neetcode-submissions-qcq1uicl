public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        var count = new Dictionary<int, int>();
        // 3: 3
        // 2: 2
        // 7: 2
        foreach (var n in nums) {
            count[n] = count.GetValueOrDefault(n, 0) + 1;
        }
        var bucket = new List<int>[nums.Length + 1];
        for(int i = 0; i < bucket.Length; i++) {
            bucket[i] = new List<int>();
        }

        foreach (var entry in count) {
            bucket[entry.Value].Add(entry.Key);
        }

        var res = new int[k];
        var index = 0;
        for (int i = bucket.Length - 1; i >= 0 && index < k; i--) {
            foreach (var n in bucket[i]) {
                res[index++] = n;
                if (index == k) {
                    return res;
                }
            }
        }
        return res;
    }
}
