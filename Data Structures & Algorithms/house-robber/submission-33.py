class Solution:
    def rob(self, nums: List[int]) -> int:
        distanceRob, adjRob = 0, 0
    
        for n in nums:
            tmp = max(n + distanceRob, adjRob)
            distanceRob = adjRob
            adjRob = tmp
        return adjRob