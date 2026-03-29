class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for key, value in count.items():
            freq[value].append(key)

        res = []
        for f in range(len(freq) - 1, -1, -1):
            for n in freq[f]:
                res.append(n)
                if len(res) == k:
                    return res
        return []
        