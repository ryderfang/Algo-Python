#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from functools import reduce
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        def reduce_func(a: List[List[int]], b: List[int]):
            if len(a) == 0:
                return [b]
            merged = False
            for i, x in enumerate(a):
                if x[0] > b[1]:
                    a.insert(i, b)
                    merged = True
                    break
                elif x[0] <= b[1] and x[1] >= b[0]:
                    a = a[0:i] + [[min(x[0], b[0]), max(x[1], b[1])]] + a[i+1:]
                    merged = True
                    break
            if not merged:
                a.append(b)
            return a
        ans = reduce(reduce_func, intervals, [])
        return ans
        
# @lc code=end

