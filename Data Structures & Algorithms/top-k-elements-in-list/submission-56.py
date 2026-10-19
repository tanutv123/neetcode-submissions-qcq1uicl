class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        
        freq = [[] for _ in range(len(nums) + 1)]
        for key, value in cnt.items():
            freq[value].append(key)
        
        res = []
        for i in range(len(freq) -1 , -1, -1):
            currFreq = freq[i]
            for f in currFreq:
                res.append(f)
                if len(res) == k:
                    return res
        return []

