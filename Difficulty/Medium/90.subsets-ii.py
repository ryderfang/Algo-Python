#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
from typing import List
import sys

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        nums.sort()
        count = len(nums)
        # 存脚标
        def _getNext(pre: List[int]) -> List[List[int]]:
            sz = len(pre)
            maxIdx = (pre[-1] + 1) if sz > 0 else 0
            ret = []
            i = maxIdx
            while i < count:
                ret.append(pre + [i])
                # 相同的只加一次
                while i < count - 1 and nums[i+1] == nums[i]:
                    i += 1
                i += 1
            return ret
        i = 0
        while i < len(ans):
            ans.extend(_getNext(ans[i]))
            i += 1
        # 恢复成数字
        t_ans = []
        for x in ans:
            tmp = [nums[j] for j in x]
            t_ans.append(tmp)
        return t_ans
# @lc code=end

