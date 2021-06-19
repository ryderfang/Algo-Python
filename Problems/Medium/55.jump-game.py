#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        sz = len(nums)
        furthest = 0 
        for i, n in enumerate(nums[0:sz-1]):
            if i <= furthest < i + n:
                furthest = i + n
            # opt
            if furthest >= sz - 1:
                break
        return True if (furthest >= sz - 1) else False
# @lc code=end

