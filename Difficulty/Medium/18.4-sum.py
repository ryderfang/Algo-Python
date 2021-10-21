#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sz = len(nums)
        if sz < 4:
            return []
        ans = []
        nums.sort()
        for a in range(sz-3):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            # opt
            if 4 * nums[a] > target:
                break
            # opt
            if nums[a] + 3 * nums[-1] < target:
                continue
            for b in range(a+1, sz-2):
                if b > a + 1 and nums[b] == nums[b-1]:
                    continue
                # opt
                if nums[a] + 3 * nums[b] > target:
                    break
                # opt
                if nums[a] + nums[b] + 2 * nums[-1] < target:
                    continue
                c = b + 1
                d = sz - 1
                while c < d:
                    # opt
                    if nums[a] + nums[b] + 2 * nums[c] > target:
                        break
                    # opt
                    if nums[a] + nums[b] + nums[c] + nums[-1] < target:
                        c += 1
                        continue
                    tt = nums[a] + nums[b] + nums[c] + nums[d]
                    if tt == target:
                        ans.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                        while c < d and nums[c] == nums[c-1]:
                            c += 1
                        while c < d and nums[d] == nums[d+1]:
                            d -= 1
                    elif tt > target:
                        d -= 1
                    else:
                        c += 1
        return ans

# @lc code=end

