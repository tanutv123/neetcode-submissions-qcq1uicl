public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var set = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++) {
            var current = target - nums[i];
            if (set.ContainsKey(nums[i])) {
                return [set[nums[i]], i];
            }
            set.Add(current, i);
        }
        return [];
    }
}
