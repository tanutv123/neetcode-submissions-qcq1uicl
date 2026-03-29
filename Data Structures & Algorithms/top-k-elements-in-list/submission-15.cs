public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        Dictionary<int, int> count = new Dictionary<int, int>();
        List<int>[] freq = new List<int>[nums.Length + 1];
        var res = new int[k];
        for(int i = 0; i < freq.Length; i++) {
            freq[i] = new List<int>();
        }

        for(int i = 0; i < nums.Length; i++) {
            if(count.ContainsKey(nums[i])) {
                count[nums[i]]++;
            } else {
                count[nums[i]] = 1;
            }
        }

        foreach(var entry in count) {
            freq[entry.Value].Add(entry.Key);
        }

        var index = 0;
        for(int i = freq.Length - 1; i >= 0 && index < k; i--) {
            foreach(var num in freq[i]) {
                res[index++] = num;
                if(index == k) {
                    return res;
                }
            }
        }
        return res;

    }
}
