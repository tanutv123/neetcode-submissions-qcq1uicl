class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        res = [0] * len(nums)
        product = 1
        for n in nums:
            if not n:
                zero_cnt += 1
            else:
                product *= n
        
        if zero_cnt > 1: return [0] * len(nums)

        for i, n in enumerate(nums):
            if zero_cnt: res[i] = 0 if n else product
            else: res[i] = product // n
        return res
