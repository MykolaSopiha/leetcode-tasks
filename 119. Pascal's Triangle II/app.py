from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for i in range(rowIndex+1):
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(result[-1][j]+result[-1][j-1])
            result.append(row)
            if i>1: result = result[-2:]
        return result[-1]
