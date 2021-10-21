#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # def swap(nums: List[int], a, b):
        #     tmp = nums[b]
        #     nums[b] = nums[a]
        #     nums[a] = tmp
        sz = len(nums)
        if sz == 1:
            return
        i = sz - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            j = sz - 1
            while j > i and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            nums[i+1:] = nums[i+1:][::-1]
        else:
            nums.reverse()
        return nums

        
# @lc code=end

