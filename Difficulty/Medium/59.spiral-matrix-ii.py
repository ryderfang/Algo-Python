#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [x[:] for x in [[-1] * n] * n]
        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        i, j, idx, v = 0, 0, 0, 2
        target = n * n + 1
        ans[0][0] = 1
        while v < target:
            tx = i + d[idx][0]
            ty = j + d[idx][1]
            if 0 <= tx < n and 0 <= ty < n and ans[tx][ty] < 0:
                i, j = tx, ty
                ans[i][j] = v
                v += 1
            else:
                idx = (idx + 1) % 4
        return ans

# @lc code=end

