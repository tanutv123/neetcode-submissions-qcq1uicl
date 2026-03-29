public class Solution {
            public int[] TwoSum(int[] nums, int target)
        {
            Dictionary<int, List<int>> diffList = new Dictionary<int, List<int>>();
            for (int i = 0; i < nums.Length; i++)
            {
                var difference = target - nums[i];
                if (diffList.ContainsKey(nums[i]))
                {
                    diffList[nums[i]].Add(i);
                    var result = new int[2] { diffList[nums[i]].FirstOrDefault(), diffList[nums[i]].LastOrDefault() };
                    return result;
                }

                if (!diffList.ContainsKey(difference))
                {
                    diffList[difference] = new List<int> { i };
                }
                else
                {
                    diffList[difference].Add(i);
                }
            }
            return null;
        }

}
