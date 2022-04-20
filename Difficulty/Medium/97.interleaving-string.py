#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
from distutils.dir_util import copy_tree
from re import I


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        sz1 = len(s1)
        sz2 = len(s2)
        sz3 = len(s3)
        if sz1 + sz2 != sz3:
            return False
        if sz1 == 0:
            return s2 == s3
        if sz2 == 0:
            return s1 == s3
        dp = [[-1 for j in range(sz2+1)] for i in range(sz1+1)] 
        # s1 取 i 个，s2 取 j 个
        dp[0][0] = 1
        for i in range(0, sz1 + 1):
            for j in range(0, sz2 + 1):
                if dp[i][j] > 0:
                    continue
                if i > 0 and dp[i-1][j] > 0 and s3[i+j-1] == s1[i-1]:
                    dp[i][j] = 1
                if j > 0 and dp[i][j-1] > 0 and s3[i+j-1] == s2[j-1]:
                    dp[i][j] = 1
        ans = dp[sz1][sz2] > 0
        return ans

# @lc code=end

