#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
from typing import List
import itertools
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sz = len(nums)
        ret = [[]]
        cnt = 1
        while cnt <= sz:
            idx = list(itertools.combinations(range(sz), cnt))
            for x in idx:
                ret.append([nums[i] for i in list(x)])
            cnt += 1
        return ret
        
# @lc code=end

