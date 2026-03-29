class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffList = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in diffList:
                return [diffList[diff], i]
            else:
                diffList[n] = i
        return [0, 0]
