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

        sz = len(candidates)
        total = [ 0 ] * (sz + 1)
        i = sz - 1
        for x in reversed(candidates):
            total[i] = total[i+1] + x
            i -= 1

        def getAns(candidates, start, target):
            nonlocal sz
            if start == sz:
                return []
            x = candidates[start]
            if start == (sz - 1):
                if target == x:
                    return [[x]]
                else:
                    return []
            # opt
            if x > target:
                return []
            else:
                nonlocal total
                # opt
                if total[start] < target:
                    return []
                tmp = []
                # pick x
                if x < target:
                    other = getAns(candidates, start + 1, target - x)
                    if len(other) > 0:
                        for t in other:
                            tmp.append([x] + t)
                else:
                    tmp.append([x])
                # not pick x
                other = getAns(candidates, start + 1, target)
                if len(other) > 0:
                    tmp = tmp + other
                
                # distinct
                tmp = map(lambda x: tuple(x), tmp)
                tmp = list(set(tmp))
                tmp = map(lambda x: list(x), tmp)
                return list(tmp)

        return getAns(candidates, 0, target)
# @lc code=end

