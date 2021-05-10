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
        st = set()
        for i in range(sz):
            p, q = i - 1, i + 1
            while p >= 0 and q < sz:
                total = nums[i] + nums[p] + nums[q]
                if total == 0:
                    st.add(str(nums[p]) + ',' + str(nums[i]) + ',' + str(nums[q]))
                    p -= 1
                    q += 1
                elif total > 0:
                    p -= 1
                else:
                    q += 1
        ans = []
        for x in st:
            tmp = x.split(',')
            for i in range(len(tmp)):
                tmp[i] = int(tmp[i])
            ans.append(tmp)
        return ans

        
# @lc code=end

