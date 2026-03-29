class Solution:
    def rob(self, nums: List[int]) -> int:
        prevRob, latestRob = 0, 0
    
        for n in nums:
            tmp = max(latestRob, prevRob + n)
            prevRob = latestRob
            latestRob = tmp
        return latestRob 