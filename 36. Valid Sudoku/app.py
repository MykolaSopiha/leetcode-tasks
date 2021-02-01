from typing import List

class Solution:
    emptyCell = '.'

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row = [x for x in row if x != self.emptyCell]
            if len(set(row)) != len(row):
                return False
        
        for columnIndex in range(9):
            column = []
            for rowIndex in range(9):
                if board[rowIndex][columnIndex] != self.emptyCell:
                    column.append(board[rowIndex][columnIndex])
            if len(set(column)) != len(column):
                return False

        for rw in range(3):
            for cl in range(3):
                subBoard = []
                for i in range(3):
                    for j in range(3):
                        if board[3*rw + i][3*cl + j] != self.emptyCell:
                            subBoard.append(board[3*rw + i][3*cl + j])
                if len(set(subBoard)) != len(subBoard):
                    return False

        return True