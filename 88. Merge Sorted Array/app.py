from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0: return nums1

        for i in range(m, m+n):
            nums1[i] = None

        i = j = 0
        while i < m + n and j < n:
            if nums1[i] == None or nums1[i] >= nums2[j]:
                nums1.insert(i, nums2[j])
                nums1.pop()
                j += 1
            i += 1

        return nums1