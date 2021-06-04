#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        sz = len(nums)
        ans = [ 10 ** 5 ] * sz
        ans[0] = 0
        for i in range(sz):
            for j in range(1, nums[i] + 1):
                if i + j < sz:
                    ans[i + j] = min(ans[i + j], ans[i] + 1)
                else:
                    break
        return ans[sz-1]
        
# @lc code=end

