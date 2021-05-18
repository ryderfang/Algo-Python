#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        sz = len(nums)
        left = 0
        right = sz - 1
        while left < right and nums[left] > nums[right]:
            mid = (left + right) // 2
            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid
        k = sz - left - 1

        left = 0
        right = sz - 1
        # target -> [0, k)
        if nums[0] > target:
            left = sz - k
        else:
            right = sz - k - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                ans = mid
                break
        return ans

# @lc code=end

