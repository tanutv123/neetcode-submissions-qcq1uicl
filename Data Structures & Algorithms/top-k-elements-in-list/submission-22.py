class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for n in range(len(nums) + 1)]
        res = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, f in count.items():
            freq[f].append(n)
        for f in range(len(freq) - 1, 0, -1):
            for n in freq[f]:
                res.append(n)
                if len(res) == k:
                    return res
