#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = self.countAndSay(n - 1)
        i, ans = 0, ""
        sz = len(s)
        while i < sz:
            cnt = 0
            t = s[i]
            while i < sz and s[i] == t:
                cnt += 1
                i += 1
            ans += str(cnt) + t
        return ans

# @lc code=end

