from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        for candidate in candidates:
            i = 1
            rest = target - i * candidate

            while rest >= 0:
                if rest == 0:
                    result += [i * [candidate]]
                    break
                elif rest in candidates:
                    result += [(i * [candidate]) + [rest]] 

                i += 1
                rest = target - i * candidate

        return result
