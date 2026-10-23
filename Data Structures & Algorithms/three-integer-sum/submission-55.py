class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[r] + nums[l]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
                    while r >= 0 and nums[r] == nums[r + 1]:
                        r -= 1
        return res