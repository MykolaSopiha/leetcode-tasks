from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        overflow = True
        i = len(digits) - 1

        while overflow and i >= 0:
            digits[i] = digits[i] + 1
            overflow = digits[i] > 9
            digits[i] = digits[i] % 10
            i = i - 1
        
        if overflow:
            digits = [1] + digits

        return digits


