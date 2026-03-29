class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def dfs(n):
            if n == len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[n])
            dfs(n + 1)
            curr.pop()

            dfs(n + 1)
        
        dfs(0)
        return res