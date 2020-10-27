from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i1 = i2 = 0
        merged = []

        while i1 < len(nums1) or i2 < len(nums2):
            if i1 == len(nums1):
                merged += nums2[i2:]
                break
            elif i2 == len(nums2):
                merged += nums1[i1:]
                break

            if nums1[i1] < nums2[i2]:
                merged.append(nums1[i1])
                i1 += 1
            else:
                merged.append(nums2[i2])
                i2 += 1
        
        if len(merged) % 2 == 1:
            return merged[int((len(merged) - 1)/2)]
        else:
            num1 = merged[int( len(merged) / 2 )]
            num2 = merged[int( (len(merged) - 1)/2 )]
            return (num1 + num2)/2