class Solution:
    def rob(self, nums: List[int]) -> int:
        prevRob, latestRob = 0, 0

        for n in nums:
            currentRob = max(latestRob, prevRob + n)
            prevRob = latestRob
            latestRob = currentRob

        return latestRob