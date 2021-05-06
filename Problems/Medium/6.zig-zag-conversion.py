#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        sz = len(s)
        col = 1000
        if numRows == 1:
            return s
        mp = [["" for i in range(col)] for j in range(numRows)]
        r, c = 0, 0
        for x in range(sz):
            mp[r][c] = s[x]
            if (x // (numRows - 1)) & 1:
                r -= 1
                c += 1
            else:
                r += 1
        ans = ""
        col = c + 1
        for i in range(numRows):
            for j in range(col):
                if len(mp[i][j]) > 0:
                    ans += mp[i][j]
        return ans

# @lc code=end

