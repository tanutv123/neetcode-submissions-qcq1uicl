public class Solution {
    public int FindMin(int[] nums) {
        int l = 0, r = nums.Length - 1;

        while(l < r) {
            int m = (l + r) / 2;
            if(nums[m] < nums[r]) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        return nums[l];
    }
}
