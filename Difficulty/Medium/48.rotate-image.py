#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #!!! modify self
        # (i, j) -> (j, n-1-i) -> (n-1-i, n-1-j) -> (n-1-j, i) -> (i, j)
        sz = len(matrix[0])
        for i in range(sz // 2):
            for j in range((sz + 1) // 2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[sz-1-j][i]
                matrix[sz-1-j][i] = matrix[sz-1-i][sz-1-j]
                matrix[sz-1-i][sz-1-j] = matrix[j][sz-1-i]
                matrix[j][sz-1-i] = tmp
        
# @lc code=end

