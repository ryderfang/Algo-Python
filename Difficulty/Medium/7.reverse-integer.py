#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        # [-2147483648, 2147483647]
        if x == 0:
            return 0
        arr = []
        tmp = 0
        if x > 0:
            tmp = x // 10
            arr.append(x % 10)
        else:
            arr.append(-(x % -10))
            tmp = x // -10
        while tmp > 0:
            arr.append(tmp % 10)
            tmp = tmp // 10
        sz = len(arr)
        # x = (10 ^ (sz - 1)) * a + b
        b = arr[-1]
        tmp = 1
        ans = 0
        for i in range(sz - 2, -1, -1):
            ans += (tmp * arr[i])
            tmp *= 10
        if x > 0:
            if ans > ((2147483647 - b) // 10):
                return 0
            else:
                return (10 * ans + b)
        else:
            if ans > ((2147483648 - b) // 10):
                return 0
            else:
                return -(10 * ans + b)
            
# @lc code=end

