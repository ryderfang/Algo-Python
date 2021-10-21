#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
from typing import List
import sys
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        tmp = sys.maxsize
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # same line
                    for k in range(n):
                        if k == j:
                            continue
                        if matrix[i][k] == 0:
                            continue
                        else:
                            matrix[i][k] = tmp
                    # same row
                    for k in range(m):
                        if k == i:
                            continue
                        if matrix[k][j] == 0:
                            continue
                        else:
                            matrix[k][j] = tmp
        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == tmp:
                    matrix[i][j] = 0
        return matrix
        
# @lc code=end

