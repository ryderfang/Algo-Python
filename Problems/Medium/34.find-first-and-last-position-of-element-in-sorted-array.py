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
        if sz == 0:
            return [-1, -1]
        left = 0
        right = sz - 1
        while left < right and nums[left] < nums[right]:
            if nums[left] == target and nums[right] == target:
                break
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                if nums[left] < target:
                    left += 1
                if nums[right] > target:
                    right -= 1
                
        if nums[left] != target:
            return [-1, -1]
        else:
            return [left, right]
        
# @lc code=end

