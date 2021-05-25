#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sz = len(candidates)
        if sz == 0:
            return []
        x = candidates[0]
        if sz == 1:
            if target % x == 0:
                return [[x] * (target // x)]
            else:
                return []
        cnt = 0
        ans = []
        while x * cnt <= target:
            left = target - x * cnt
            other = self.combinationSum(candidates[1:], left)
            if len(other) > 0:
                for t in other:
                    ans.append([x] * cnt + t)
            cnt += 1
        return ans

# @lc code=end

