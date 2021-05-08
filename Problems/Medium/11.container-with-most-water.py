#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height) - 1
        while left < right:
            dist = right - left
            if ans > (10 ** 4) * dist:
                break
            ans = max(ans, min(height[left], height[right]) * dist)
            # 这种情况 area([left, right]) > area([left+1, right])
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return ans

# @lc code=end

# @lc comment
"""
两边向中间逼近，移动 height 小的才有可能获得更大面积的机会。
"""
