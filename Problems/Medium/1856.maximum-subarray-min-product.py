#
# @lc app=leetcode id=1856 lang=python3
#
# [1856] Maximum Subarray Min-Product
#

# @lc code=start

INF = 10 ** 9 + 7
from typing import List
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        ans = 0
        sz = len(nums)
        # store sum[i]
        sum = [nums[0]]
        for n in nums[1:]:
            sum.append(sum[-1] + n)
        for i in range(sz):
            left = i - 1
            right = i + 1
            while left >= 0 and nums[left] >= nums[i]:
                left -= 1
            while right < sz and nums[right] >= nums[i]:
                right += 1
            right = min(right, sz - 1)
            total = nums[i] * (sum[right] - (sum[left] if left >= 0 else 0))
            ans = max(ans, total)
        ans %= INF
        return ans

# @lc code=end

