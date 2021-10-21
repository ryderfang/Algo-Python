#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
int_min = -2147483648
int_max = 2147483647
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == int_min and divisor == -1:
            return int_max
        up = abs(dividend)
        down = abs(divisor)
        ans = 0
        for x in range(32)[::-1]:
            if (up >> x) - down >= 0:
                ans += (1 << x)
                up -= (down << x)
        ans = ans if ((dividend > 0) == (divisor > 0)) else -ans
        return ans

# @lc code=end

