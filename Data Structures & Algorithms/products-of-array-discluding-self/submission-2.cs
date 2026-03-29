public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        var result = new List<int>();
        for(int i = 0; i < nums.Length; i++) {
            var product = 1;
            for(int j = 0; j < nums.Length; j++) {
                if(i != j) {
                    product = product * nums[j];
                }
            }
            result.Add(product);
        }
        return result.ToArray();
    }
}
