class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        product = 1
        zero_cnt = 0

        for n in nums:
            if n:
                product *= n
            else:
                zero_cnt += 1
        
        if zero_cnt > 1:
            return res
        
        for i, n in enumerate(nums):
            if zero_cnt:
                res[i] = 0 if n else product
            else:
                res[i] = int(product / n)
        return res