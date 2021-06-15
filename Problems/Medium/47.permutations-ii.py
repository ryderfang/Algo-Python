#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
from typing import List
from functools import reduce
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def reduce_func(a: List[int], n: int):
            tmp = []
            print(a, n)
            for l in a:
                for i in range((l + [n]).index(n) + 1):
                    tmp.append(l[:i]+[n]+l[i:])
            return tmp
        ans = reduce(reduce_func, nums, [[]])
        return ans
# @lc code=end

# best solution:
# from functools import reduce
# def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#   return reduce(lambda a,n:[l[:i]+[n]+l[i:] for l in a for i in range((l+[n]).index(n)+1)], nums,[[]])