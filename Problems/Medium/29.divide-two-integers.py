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
        positive = True
        if dividend > 0 and divisor < 0:
            divisor = -divisor
            positive = False
        if dividend < 0 and divisor > 0:
            dividend = -dividend
            positive = False
        if dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor
        result = dividend // divisor
        if not positive:
            result = -result
        return result

# @lc code=end

