from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2: 
            return len(nums)

        i = 1

        while (i < len(nums)):
            if nums[i - 1] == nums[i]:
                nums.pop(i)
            else:
                i += 1
        
        return len(nums)