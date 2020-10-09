from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsIndexes = {}

        for i1 in range(len(nums)):
            complement = target - nums[i1]

            if complement in numsIndexes:
                return [i1, numsIndexes[complement]]
            else:
                numsIndexes[nums[i1]] = i1