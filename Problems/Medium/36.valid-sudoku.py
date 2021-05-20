#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ans = True
        def hasRepetition(nums: List[str]):
            s = set()
            cnt = 0
            for i in range(9):
                if nums[i] != '.':
                    s.add(nums[i])
                    cnt += 1
            if len(s) < cnt:
                return True
            return False
        # rows
        for i in range(9):
            if hasRepetition(board[i]):
                ans = False
                break
        if not ans:
            return ans
        # columns
        for j in range(9):
            n = []
            for i in range(9):
                n.append(board[i][j])
            if hasRepetition(n):
                ans = False
                break
        if not ans:
            return ans
        # sub-boxes
        for i, j in [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]:
            n = []
            for k, l in [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]:
                n.append(board[i+k][j+l])
            if hasRepetition(n):
                ans = False
                break
        return ans
        

# @lc code=end

