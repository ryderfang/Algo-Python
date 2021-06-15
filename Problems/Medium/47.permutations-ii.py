#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
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
        def distinct_nested_list(nested_lst: List[List[int]]):
            return [list(y) for y in set([tuple(x) for x in nested_lst])]
        get_next(0)
        ans = distinct_nested_list(ans)
        return ans
# @lc code=end

# best solution:
#  return reduce(lambda a,n:[l[:i]+[n]+l[i:] for l in a for i in range((l+[n]).index(n)+1)], nums,[[]])