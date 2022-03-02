#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        sz = len(nums)
        if sz < 3:
            return sz
        p = 0
        cnt = 0
        END_SENTINEL = nums[0] - 1
        while p < sz - 1 and nums[p] > END_SENTINEL:
            q = p + 1
            if nums[q] == nums[p]:
                p = q
                q += 1
                while q < sz and nums[q] == nums[p]:
                    q += 1
                p += 1
                cnt += (q - p)
                t = 0
                while p + t < sz:
                    if q + t < sz:
                        nums[p + t] = nums[q + t]
                    else:
                        nums[p + t] = END_SENTINEL
                    t += 1
            else:
                p += 1
        return (sz - cnt)
        
# @lc code=end

