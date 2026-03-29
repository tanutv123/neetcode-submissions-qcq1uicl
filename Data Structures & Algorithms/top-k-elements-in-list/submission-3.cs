public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        Dictionary<int, int> count = new Dictionary<int, int>();
        foreach(var num in nums) {
            if(!count.ContainsKey(num)) {
                count[num] = 1;
            }
            count[num]++;
        }
        List<int[]> rankArr = count.Select(entry => new int[] { entry.Value, entry.Key }).ToList();
        rankArr.Sort((a, b) => b[0].CompareTo(a[0]));

        int[] res = new int[k];
        for(int i = 0; i < k; i++) {
            res[i] = rankArr[i][1];
        }
        return res;
    }
}