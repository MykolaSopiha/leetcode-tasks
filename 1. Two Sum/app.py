from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i1 in range(len(nums)):
            try:
                i2 = nums.index(target - nums[i1])
                if i1 != i2:
                    return [i1, i2]
            except ValueError:
                pass