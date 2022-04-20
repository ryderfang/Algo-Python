#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
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
        # s2 取 i 个, s1 取 dp[i] 个，能组成 s3[:i+dp[i]]
        dp = [-1 for j in range(sz2 + 1)]
        dp[0] = 0
        if s3[0] == s1[0]:
            dp[0] = 1
        if s3[0] == s2[0]:
            dp[1] = 0
        for i in range(0, sz1 + 1):
            for j in range(0, sz2 + 1):
                if dp[j] == i:
                    continue
                if i > 0 and dp[j] == i - 1 and s3[i+j-1] == s1[i-1]:
                    dp[j] = i
                if j > 0 and dp[j-1] == i and s3[i+j-1] == s2[j-1]:
                    dp[j] = i
        ans = (dp[sz2] == sz1)
        return ans

# @lc code=end

