from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_indexes = {}

        for i1 in range(len(nums)):
            complement = target - nums[i1]

            if complement in nums_indexes:
                return [i1, nums_indexes[complement]]
            else:
                nums_indexes[nums[i1]] = i1