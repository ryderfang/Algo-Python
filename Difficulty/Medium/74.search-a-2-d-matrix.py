#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        def getPos(index: int):
            return [index // n, index - (index // n) * n]
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            [x, y] = getPos(mid)
            if matrix[x][y] > target:
                right = mid - 1
            elif matrix[x][y] < target:
                left = mid + 1
            else:
                return True
        return False
# @lc code=end

