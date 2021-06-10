#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sz = len(nums)
        ans = []
        def swap(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        def get_next(start: int):
            if start == sz - 1:
                ans.append(nums.copy())
            for i in range(start, sz):
                swap(i, start)
                get_next(start + 1)
                swap(i, start)
        get_next(0)
        return ans
                
# @lc code=end

