#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        def find(i: int, j: int, v: dict, s: str):
            if board[i][j] != s[0] or v.get(i * n + j, 0):
                return False
            if len(s) == 1 and board[i][j] == s[0]:
                print(i, j)
                return True
            ret = False
            d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            for k in d:
                if i + k[0] >= 0 and i + k[0] < m and j + k[1] >= 0 and j + k[1] < n:
                    v[i * n + j] = 1
                    if find(i + k[0], j + k[1], v, s[1:]):
                        print(i, j)
                        return True
                    else:
                       v[i * n + j] = 0
            return False
        v = {}
        for i in range(m):
            for j in range(n):
                v.clear()
                if find(i, j, v, word):
                    return True
        return False
        
# @lc code=end

