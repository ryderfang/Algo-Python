#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        ans = [x[:] for x in [[1] * n] * m]
        def pre_process():
            for i in range(1, m):
                for j in range(1, n):
                    ans[i][j] = ans[i][j-1] + ans[i-1][j]
        pre_process()
        return ans[m-1][n-1]
# @lc code=end

