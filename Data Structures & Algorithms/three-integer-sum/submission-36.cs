public class Solution {
    public List<List<int>> ThreeSum(int[] nums) {
        Array.Sort(nums);
        List<List<int>> res = new List<List<int>>();

        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] > 0) {
                break;
            }

            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int l = i + 1, r = nums.Length - 1;

            while (l < r) {
                int threeSum = nums[i] + nums[l] + nums[r];
                if (threeSum > 0) {
                    r -= 1;
                } else if (threeSum < 0) {
                    l += 1;
                } else {
                    res.Add(new List<int> { nums[i], nums[l], nums[r] });
                    l += 1;
                    r -= 1;

                    while (l < r && nums[l] == nums[l - 1]) {
                        l += 1;
                    }
                }
            }
        }
        return res;  // Moved outside the loop
    }
}
