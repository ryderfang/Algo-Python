#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        tmp = []
        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if n != '.':
                    tmp.extend([(i, n), (n, j), (i // 3, j // 3, n)])
        return len(tmp) == len(set(tmp))

# @lc code=end

