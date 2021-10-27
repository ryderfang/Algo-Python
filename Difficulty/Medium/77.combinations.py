#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
from typing import List
import itertools
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        tmp = [i for i in range(1, n + 1)]
        return list(itertools.combinations(tmp, k))
        
# @lc code=end

