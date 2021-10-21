#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sz = len(nums)
        p = 0
        for i, x in enumerate(nums):
            if x < 0 or x > sz:
                nums[i] = 0
        while p < sz:
            if nums[p] == (p + 1):
                p += 1
                continue
            q = nums[p]
            nums[p] = 0
            while q > 0:
                tmp = nums[q - 1]
                if tmp == q:
                    break
                else:
                    nums[q - 1] = q
                    q = tmp
            p += 1
        for i, x in enumerate(nums):
            if x == (i + 1):
                continue
            if x == 0:
                return (i + 1)
        return sz + 1
                
            
# @lc code=end

