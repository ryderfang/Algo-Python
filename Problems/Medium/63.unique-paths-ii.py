#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        ans = [x[:] for x in [[0] * n] * m]
        ans[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, m):
            ans[i][0] = ans[i-1][0] if not obstacleGrid[i][0] else 0
        for j in range(1, n):
            ans[0][j] = ans[0][j-1] if not obstacleGrid[0][j] else 0
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    ans[i][j] = 0
                else:
                    ans[i][j] = (ans[i][j-1] if not obstacleGrid[i][j-1] else 0) + (ans[i-1][j] if not obstacleGrid[i-1][j] else 0)
        return ans[m-1][n-1]
# @lc code=end

