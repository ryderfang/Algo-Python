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
        sz = len(nums)
        # store sum[i]
        sum = [nums[0]]
        for n in nums[1:]:
            sum.append(sum[-1] + n)
        left = [-1 for i in range(sz)]
        right = [-1 for i in range(sz)]
        for i in range(1, sz):
            if nums[i] > nums[i-1]:
                left[i] = i - 1
            else:
                j = left[i-1]
                while j >= 0 and nums[j] >= nums[i]:
                    j -= 1
                left[i] = j
        right[sz-1] = sz
        for i in range(sz-2, -1, -1):
            if nums[i] > nums[i+1]:
                right[i] = i + 1
            else:
                j = right[i+1]
                while j < sz and nums[j] >= nums[i]:
                    j += 1
                right[i] = j
        ans = 0
        for i in range(sz):
            total = nums[i] * (sum[right[i]-1] - (sum[left[i]] if left[i] >= 0 else 0))
            ans = max(ans, total)
        ans %= INF
        return ans

# @lc code=end

