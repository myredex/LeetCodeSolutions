"""
https://leetcode.com/problems/valid-sudoku/
36. Valid Sudoku
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
import collections
from typing import List

case_1 = [["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]]

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        sqr = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if (val in row[r]
                    or val in col[c]
                    or val in sqr[(r // 3, c // 3)]):
                    return False
                row[r].add(val)
                col[c].add(val)
                sqr[(r // 3, c // 3)].add(val)
        return True

print(Solution().isValidSudoku(case_1))