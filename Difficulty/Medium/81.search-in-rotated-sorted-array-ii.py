#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
from typing import List
class Solution:
    # samilar with p33
    def search(self, nums: List[int], target: int) -> bool:
        sz = len(nums)
        # 有重复元素怎么二分找 k
        l = 0
        while l < sz - 2 and nums[l+1] >= nums[l]:
            l += 1
        k = sz - 1 - l
        print(k)

        def _bsearch(l, r):
            if l > r:
                return False
            while l < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return nums[l] == target
        # [0, l] 和 [l+1, sz-1] 分别是两个非递减列表 
        return _bsearch(0, l) or _bsearch(l+1, sz-1)
        
# @lc code=end

