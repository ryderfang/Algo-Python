#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        sz = len(s)
        # 结尾 1 位
        f = [0 for i in range(sz)]
        # 结尾 2 位
        g = [0 for i in range(sz)]
        if int(s[0]) >= 1 and int(s[0]) <= 9:
            f[0] = 1
        for i in range(1, sz):
            n1 = int(s[i])
            n2 = int(s[i-1])
            if n1 >= 1 and n1 <= 9:
                f[i] = f[i-1] + g[i-1]
            else:
                f[i] = 0
            if (n2 == 1 and n1 >= 0 and n1 <= 9) or \
                (n2 == 2 and n1 >= 0 and n1 <= 6):
                g[i] = (f[i-2] + g[i-2]) if i > 1 else 1
            else:
                g[i] = 0
        return f[sz-1] + g[sz-1]
        
# @lc code=end

