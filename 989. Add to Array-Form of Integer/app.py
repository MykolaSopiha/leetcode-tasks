from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        _str = k + int(''.join(map(str,num)))
        return [int(x) for x in str(_str)]