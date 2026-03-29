class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for val, key in count.items():
            freq[key].append(val)
        
        res = []

        for i in range(len(freq) - 1, 0, -1):
            for val in freq[i]:
                res.append(val)
                if len(res) == k:
                    return res