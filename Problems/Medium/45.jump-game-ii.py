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
        if sz == 1:
            return 0
        ans = [0] * sz
        # furthest pos
        tmp = 0
        for i, n in enumerate(nums):
            if i + n > tmp:
                ans[tmp+1:i+n+1] = [ans[i] + 1] * (i+n-tmp)
                tmp = i + n
                # opt
                if i + n >= sz - 1:
                    break
        return ans[-1]
    
# @lc code=end

