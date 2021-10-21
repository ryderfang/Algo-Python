#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        n = len(nums)
        while i < n:
            # find not zero
            while i < n and nums[i] == 0:
                i += 1
            if i >= n:
                break
            if nums[i] == 1:
                j = i + 1
                while j < n and nums[j] != 0:
                    j += 1
                # swap 0(nums[j]) with 1(nums[i])
                if j < n:
                    tmp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = tmp
                i += 1
            elif nums[i] == 2:
                j = i + 1
                k = -1
                while j < n and nums[j] != 0:
                    if k < 0 and nums[j] == 1:
                        k = j
                    j += 1
                if j < n:
                    # find 0, swap 0(nums[j]) with 2(nums[i])
                    tmp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = tmp
                    i += 1
                elif k > 0:
                    # find 1, swap 1(nums[k]) with 2(nums[i])
                    tmp = nums[k]
                    nums[k] = nums[i]
                    nums[i] = tmp
                    i += 1
                else:
                    # is all 2 from i to n
                    break
        pass
# @lc code=end

