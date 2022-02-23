#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
from ast import Not
from inspect import _void
from os import unsetenv
from re import I
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        fa = {}
        def _find(x) -> int:
            if x == fa[x]:
                return x
            else:
                fa[x] = _find(fa[x])
                return fa[x]
        for x in nums:
            fa[x] = x
        for x in nums:
            if x + 1 in fa:
                fa[x] = x + 1
        ret = 0
        for x in nums:
            r = _find(x)
            h = r - x + 1
            if ret < h:
                ret = h
        return ret
# @lc code=end

