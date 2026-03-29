class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] 

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        n = len(freq)
        res = [] * k
        for f in range(n - 1, -1, -1):
            for n in freq[f]:
                res.append(n)
                if (len(res) == k):
                    return res
