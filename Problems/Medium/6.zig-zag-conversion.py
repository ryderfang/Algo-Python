#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution:
    # k -> 2*(r-1)-k -> 4*(r-1)-k -> 6*(r-1)-k
    def convert(self, s: str, numRows: int) -> str:
        sz = len(s)
        r = numRows
        if r == 1:
            return s
        ans = ""
        for i in range(r):
            if i >= sz:
                break
            ans += s[i]
            fact = 2
            while (idx := fact * (r - 1) - i) and idx < sz:
                if i != 0 and i != r - 1:
                    ans += s[idx]
                idx = fact * (r - 1) + i
                if idx < sz:
                    ans += s[idx]
                fact += 2
        return ans

# @lc code=end

