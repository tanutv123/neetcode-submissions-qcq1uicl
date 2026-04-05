public class Solution
{
    public int[] TopKFrequent(int[] nums, int k)
    {
        var freq = new List<int>[nums.Length + 1];
        for (int i = 0; i < freq.Length; i++)
        {
            freq[i] = [];
        }
        var dict = new Dictionary<int, int>();
        foreach (var n in nums)
        {
            if (dict.ContainsKey(n)) {
                dict[n]++;
            } else {
                dict[n] = 1;
            }
        }

        foreach (var entry in dict) {
            freq[entry.Value].Add(entry.Key);
        }

        var res = new int[k];
        var index = 0;
        for (int i = freq.Length - 1; i >= 0 && index != k; i--)
        {
            foreach (var n in freq[i])
            {
                res[index] = n;
                index++;
                if (index == k)
                {
                    return res;
                }
            }
        }
        return [];
    }
}

