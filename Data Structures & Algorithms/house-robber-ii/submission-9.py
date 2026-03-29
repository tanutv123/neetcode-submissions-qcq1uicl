class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:len(nums)-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for i in range(len(nums)):
            tmp = max(rob2, rob1 + nums[i])
            rob1 = rob2
            rob2 = tmp
        
        return rob2