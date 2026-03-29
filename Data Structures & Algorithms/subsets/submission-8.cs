public class Solution {
    public List<List<int>> Subsets(int[] nums) {
        var res = new List<List<int>>();
        var subSet = new List<int>();
        Dfs(0, nums, subSet, res);
        return res;
    }

    private void Dfs(int i, int[] nums, List<int> subSet, List<List<int>> res) {
        if(i == nums.Length) {
            res.Add(new List<int>(subSet));
            return;
        }
        
        subSet.Add(nums[i]);
        Dfs(i + 1, nums, subSet, res);
        subSet.RemoveAt(subSet.Count - 1);
        Dfs(i + 1, nums, subSet, res);
    }
}
