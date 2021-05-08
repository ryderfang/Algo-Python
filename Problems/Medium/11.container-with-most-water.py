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
        sz = len(height)
        # f[i] is the first one which height[f[i]] > height[i] and f[i] > i
        f = [0 for i in range(sz)]
        # b[i] is the first one which height[b[i]] > height[i] and b[i] < i
        b = [-1 for i in range(sz)]
        for j in range(sz-1, 0, -1):
            if height[j] >= height[0]:
                f[0] = j
                break
        if f[0] > 0:
            ans = max(ans, height[0] * (f[0] - 0))
            # print(ans)
        for i in range(1, sz):
            if height[i] >= height[i-1]:
                for j in range(f[i-1], i, -1):
                    if height[j] >= height[i]:
                        f[i] = j
                        break
                for k in range(b[i-1] if b[i-1] >= 0 else i, i):
                    if height[k] >= height[i]:
                        b[i] = k
                        break
            else:
                for j in range(sz - 1, f[i-1] - 1, -1):
                    if height[j] >= height[i]:
                        f[i] = j
                        break
                for k in range(0, b[i-1] + 1 if b[i-1] >= 0 else i):
                    if height[k] >= height[i]:
                        b[i] = k
                        break
            if f[i] > i:
                tmp = height[i] * (f[i] - i)
                if ans < tmp:
                    # print(tmp, height[i], i, f[i])
                    ans = tmp
            if b[i] >= 0 and b[i] < i:
                tmp = height[i] * (i - b[i])
                if ans < tmp:
                    # print(tmp, height[i], b[i], i)
                    ans = tmp
        return ans

# @lc code=end

# @lc comment
"""
在 (i, sz-1] 范围内找第一个 height[j] >= height[i] 的 j，记为 f[i] = j
在 [0, i) 范围内找第一个 height[j] >= height[i] 的 j，记为 b[i] = j
如果 height[i+1] >= height[i]，则必然 height[i+1] >= height[i] > height[f[i] + 1]，所以
f[i+1] 只可能在 [i+1, f[i]] 之间；如果 height[i+1] < height[i]，则只可能在 [f[i], sz-1] 之间
同理 height[i+1] >= height[i]，b[i+1] -> [b[i], i+1]
height[i+1] < height[i], b[i+1] -> [0, b[i]]
"""


