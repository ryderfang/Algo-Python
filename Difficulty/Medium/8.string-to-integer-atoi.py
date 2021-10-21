#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(' ')
        if len(s) == 0:
            return 0
        negative = False
        i = 0
        if s[i] == '-':
            negative = True
            i += 1
        elif s[i] == '+':
            i += 1
        elif not s[i].isdigit():
            return 0
        ans = 0
        while i < len(s):
            if not s[i].isdigit():
                break
            ans = (ans * 10) + int(s[i])
            i += 1
        if ans > 0:
            ans = -ans if negative else ans
        ans = max(min(ans, 2 ** 31 - 1), - 2 ** 31)
        return ans
        
# @lc code=end

