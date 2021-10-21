#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        top, left = 0, 0
        right = col - 1
        bottom = row - 1
        i, j = 0, 0
        ans = [matrix[i][j]]
        while len(ans) < row * col:
            # right
            while j < right:
                j += 1
                ans.append(matrix[i][j])
            top += 1
            if len(ans) >= row * col:
                break
            # bottom
            while i < bottom:
                i += 1
                ans.append(matrix[i][j])
            right -= 1
            if len(ans) >= row * col:
                break
            # left
            while j > left:
                j -= 1
                ans.append(matrix[i][j])
            bottom -= 1
            if len(ans) >= row * col:
                break
            # top
            while i > top:
                i -= 1
                ans.append(matrix[i][j])
            left += 1
            if len(ans) >= row * col:
                break
        return ans

# @lc code=end

