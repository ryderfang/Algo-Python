#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        sq = []
        for i in range(1, 101):
            sq.append(i * i)
        ret = {0: 0, 1: 1}
        for i in range(2, n + 1):
            t = 10 ** 4 + 1
            for j in sq:
                if j > i:
                    break
                if j == i:
                    t = 1
                else:
                    t = min(t, ret[i - j] + ret[j])
            ret[i] = t
        return ret[n]

# @lc code=end

