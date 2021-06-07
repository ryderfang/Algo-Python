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
        ans = [0]
        for i in range(sz):
            # opt
            if i == sz - 1:
                return ans[i]
            elif i + nums[i] >= sz - 1:
                return ans[i] + 1
            now = len(ans)
            for j in range(now, i + nums[i] + 1):
                ans.append(ans[i] + 1)
        return ans[sz - 1]
    
# @lc code=end

