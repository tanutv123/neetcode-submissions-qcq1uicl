class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, total, subSet):
            if total == target:
                res.append(subSet.copy())
                return
            
            if i == len(candidates) or total > target:
                return
            
            subSet.append(candidates[i])
            dfs(i + 1, total + candidates[i], subSet)
            subSet.pop()

            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(i + 1, total, subSet)
        
        dfs(0,0, [])
        return res