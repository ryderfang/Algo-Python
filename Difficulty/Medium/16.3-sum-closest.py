#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = 0x7fffffff
        sz = len(nums)
        nums.sort()
        for i in range(sz-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            p = i + 1
            q = sz - 1
            b = True
            while p < q:
                tmp = nums[i] + nums[p] +nums[q]
                if abs(tmp - target) < abs(ans - target):
                    ans = tmp
                if tmp == target:
                    break
                elif tmp > target:
                    q -= 1
                else:
                    p += 1
            if ans == target:
                break
        return ans


# @lc code=end

