from typing import DefaultDict, List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[int((len(nums) - 1) / 2)]
