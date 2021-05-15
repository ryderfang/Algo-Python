#
# @lc app=leetcode id=1856 lang=python3
#
# [1856] Maximum Subarray Min-Product
#

# @lc code=start

INF = 10 ** 9 + 7
from os import stat
from typing import List
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        sz = len(nums)
        # store sum[i]
        # sum = [0]
        # for n in nums:
        #     sum.append(sum[-1] + n)

        ans = 0
        stack = [(0, 0)]
        # add 0 to clear stack
        sum_i = 0
        for n in nums + [0]:
            pre_sum = sum_i
            while stack and stack[-1][1] >= n:
                pre_sum, height = stack.pop()
                ans = max(ans, height * (sum_i - pre_sum))
            stack.append((pre_sum, n))
            sum_i += n
        ans %= INF
        return ans

# @lc code=end

