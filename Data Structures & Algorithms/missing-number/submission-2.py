class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        prev = -1
        for n in sorted(nums):
            if prev + 1 != n:
                return prev + 1
            prev += 1
        return n + 1