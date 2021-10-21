#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0 
        for i, n in enumerate(nums):
            if i > furthest:
                return False
            furthest = max(furthest, i + n)
        return True
# @lc code=end

