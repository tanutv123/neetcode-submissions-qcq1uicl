public class Solution {
    public bool hasDuplicate(int[] nums) {
        List<int> exist = new List<int>();

        foreach(var n in nums) {
            if(exist.Any(x => x == n)) {
                return true;
            }
            exist.Add(n);
        }
        return false;
    }
}
