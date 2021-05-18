#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        sz = len(nums)
        ans = [-1, -1]
        left = 0
        right = sz - 1
        # 要有等于
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        if left >= sz or nums[left] != target:
            return ans
        
        ans[0] = left
        right = sz - 1
        # 要有等于
        while left <= right:
            mid = (left + right) // 2
            # 区别
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid -1
        ans[1] = right
        return ans
        
# @lc code=end

