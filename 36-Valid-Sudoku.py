from typing import List


class Solution:
    def isValidSudoku(self, board):
        for row in board:
            row = [val for val in row if val != '.']
            if len(row) != len(list(set(row))):
                return False

        for i in range(9):
            col = [row[i] for row in board]
            col = [val for val in col if val != '.']
            if len(col) != len(list(set(col))):
                return False

        for i in range(0, 9, 3):
            block = board[i:i+3]
            k = 0
            for j in range(0, 9, 3):
                final_block = block[k][j:j+3] + \
                    block[k+1][j:j+3]+block[k+2][j:j+3]
                # print(final_block)
                final_block = [val for val in final_block if val != '.']
                if len(final_block) != len(list(set(final_block))):
                    return False
        return True


Solution.isValidSudoku(Solution,
                       [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
