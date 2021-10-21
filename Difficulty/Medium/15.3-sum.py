#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        sz = len(nums)
        nums.sort()
        ans = []
        for i in range(sz-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # opt
            if nums[i] > 0:
                break
            p, q = i + 1, sz - 1
            while p < q:
                total = nums[i] + nums[p] + nums[q]
                if total == 0:
                    ans.append([nums[i], nums[p], nums[q]])
                    p += 1
                    q -= 1
                    while p < q and nums[p] == nums[p-1]:
                        p += 1
                    while q > p and nums[q] == nums[q+1]:
                        q -= 1
                elif total > 0:
                    q -= 1
                else:
                    p += 1
        return ans

        
# @lc code=end

