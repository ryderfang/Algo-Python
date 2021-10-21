#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    ##! not faster than system method -> (return x ** n)...
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        if n & 1:
            return x * self.myPow(x * x, n // 2)
        else:
            return self.myPow(x * x, n // 2)
# @lc code=end

