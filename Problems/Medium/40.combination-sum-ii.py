#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def getAns(candidates, target):
            sz = len(candidates)
            if sz == 0:
                return []
            x = candidates[0]
            if sz == 1:
                if target == x:
                    return [[x]]
                else:
                    return []
            # opt
            if x > target:
                return []
            else:
                tmp = []
                # pick x
                if x < target:
                    other = getAns(candidates[1:], target - x)
                    if len(other) > 0:
                        for t in other:
                            tmp.append([x] + t)
                else:
                    tmp.append([x])
                # not pick x
                other = getAns(candidates[1:], target)
                if len(other) > 0:
                    tmp = tmp + other
                
                # distinct
                tmp = map(lambda x: tuple(x), tmp)
                tmp = list(set(tmp))
                tmp = map(lambda x: list(x), tmp)
                return list(tmp)

        # opt, sort
        candidates.sort()
        return getAns(candidates, target)
# @lc code=end

