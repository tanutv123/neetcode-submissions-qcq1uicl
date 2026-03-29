public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        var zero_cnt = 0;
        var product = 1;
        foreach(var n in nums){
            if(n == 0) {
                zero_cnt += 1;
            } else {
                product *= n;
            }
        }

        if(zero_cnt > 1) {
            var res1 = new int[nums.Length];
            for(int i = 0; i < res1.Length; i++) {
                res1[i] = 0;
            }
            return res1;
        }
        var res = new int[nums.Length];
        for(int i = 0; i < nums.Length; i++) {
            if(zero_cnt == 0 ) {
                res[i] = product / nums[i];
            } else {
                if(nums[i] == 0) {
                    res[i] = product;
                } else {
                    res[i] = 0;
                }
            }
        }
        return res;
    }
}
