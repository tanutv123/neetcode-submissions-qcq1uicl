class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l = 0
        res = [0] * (len(nums) - k + 1)
        for r in range(len(nums)):
            if q and nums[q[0]] < nums[r]:
                q.appendleft(r)
            else:
                while q and nums[q[-1]] < nums[r]:
                    q.pop()
                q.append(r)
            
            if r - l + 1 > k:
                l += 1
                while q[0] < l:
                    q.popleft()
            if r - l + 1 == k:
                res[l] = nums[q[0]]
        return res
                