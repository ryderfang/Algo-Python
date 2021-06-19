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
        ans = [0] * sz
        ans[0] = 1
        furthest = 0 
        for i, n in enumerate(nums[0:sz-1]):
            # opt
            if not ans[i]:
                break
            if i + n > furthest:
                ans[furthest+1:i+n+1] = [ans[i]] * (i+n-furthest)
                furthest = i + n
            # opt
            if furthest > sz:
                break
        return True if ans[-1] else False
# @lc code=end

