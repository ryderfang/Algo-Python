#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # opt, sort
        candidates.sort()

        ans = []
        def getAns(comb, start, target):
            if target == 0:
                ans.append(list(comb))
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                pick = candidates[i]
                if pick > target:
                    break
                getAns(comb + [pick], i + 1, target - pick)
        getAns([], 0, target)
        return ans
# @lc code=end

