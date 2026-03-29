class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if n in diffMap:
                return [diffMap[n], i]
            diffMap[diff] = i
        