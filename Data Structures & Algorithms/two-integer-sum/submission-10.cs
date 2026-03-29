public class Solution {
    public int[] TwoSum(int[] nums, int target) {
                    int[] result = new int[2];
        Dictionary<int, List<int>> pairs = new Dictionary<int, List<int>>();
for(int i = 0; i < nums.Length; i++)
{
    var difference = target - nums[i];
    if (pairs.ContainsKey(nums[i]))
    {
        pairs[nums[i]].Add(i);
        if (pairs[nums[i]].Count == 2)
        {
            result = pairs[nums[i]].ToArray();
            Array.Sort(result);
            break;
        }
    } 
    else
    {
        pairs.Add(difference, new List<int> { i });
    }
}
return result;
    }
}
