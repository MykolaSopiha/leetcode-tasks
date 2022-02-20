from inspect import _void
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def getCombination(start: int, temp: List[int], target: int):
            if target == 0: return ans.append(temp)
            for idx in range(start, len(candidates)):
                curr = candidates[idx]
                tempTarget = target - curr
                if tempTarget >= 0:
                    getCombination(idx, temp + [curr], tempTarget)
        getCombination(0, [], target)        
        return ans
