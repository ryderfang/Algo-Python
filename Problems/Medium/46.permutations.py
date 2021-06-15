#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from typing import List
from functools import reduce
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def reduct_func(a: List[int], b: int):
            tmp = []
            print(a, b)
            for l in a:
                for i in range(len(l) + 1):
                    tmp.append(l[:i] + [b] + l[i:])
            return tmp
        ans = reduce(reduct_func, nums, [[]])
        return ans
                
# @lc code=end

