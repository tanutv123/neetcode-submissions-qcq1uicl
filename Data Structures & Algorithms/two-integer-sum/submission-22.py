class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if numSet and nums[i] in numSet:
                return [numSet[nums[i]], i]
            numSet[diff] = i
        return 

