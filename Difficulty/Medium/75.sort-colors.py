#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        c0, c1, c2 = 0, 0, 0
        for x in nums:
            if x == 0:
                c0 += 1
            elif x == 1:
                c1 += 1
            else:
                c2 += 1
        i = 0
        while c0 > 0:
            nums[i] = 0
            c0 -= 1
            i += 1
        while c1 > 0:
            nums[i] = 1
            c1 -= 1
            i += 1
        while c2 > 0:
            nums[i] = 2
            c2 -= 1
            i += 1
        pass
        
# @lc code=end

