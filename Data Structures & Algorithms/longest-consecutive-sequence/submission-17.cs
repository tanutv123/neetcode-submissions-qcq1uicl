public class Solution {
    public int LongestConsecutive(int[] nums) {
        HashSet<int> numSet = new HashSet<int>(nums);
        int res = 0;
        foreach(var n in nums) {
            if(!numSet.Contains(n - 1)) {
                int length = 1;
                while(numSet.Contains(n + length)) {
                    length += 1;
                }
                res = Math.Max(res, length);
            }
        }
        return res;
    }
}
