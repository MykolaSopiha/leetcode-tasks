from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: return ['']

        result = []
        
        for counter in range(n):
            for left in self.generateParenthesis(counter):
                for right in self.generateParenthesis(n - counter - 1):
                    result.append("({}){}".format(left, right))
        
        return result