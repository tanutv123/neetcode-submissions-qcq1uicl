class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A
        
        len1, len2 = len(A), len(B)
        total = len1 + len2
        half = total // 2
        l, r = 0, len1 - 1
        while True:
            i = l + ((r - l) // 2)
            j = half - i - 2

            left1 = A[i] if i >= 0 else float('-inf')
            left2 = B[j] if j >= 0 else float('-inf')
            right1 = A[i + 1] if i < len1 - 1 else float('inf')
            right2 = B[j + 1] if j < len2 - 1 else float('inf')

            if left1 <= right2 and left2 <= right1:
                if total % 2:
                    return min(right1, right2)
                return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                r = i - 1
            else:
                l = i + 1
        
