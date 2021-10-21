#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = ans = 0
        mp = {}
        for j in range(len(s)):
            if s[j] in mp:
                i = max(mp[s[j]] + 1, i)
            ans = max(ans, j - i + 1)
            mp[s[j]] = j
        return ans
# @lc code=end

# @lc comment
"""
ord 字符转换成 unicode 整数
chars/map 记录当前字符出现的位置
如果 s[j] 在 [i, j) 中出现在 j'，则 从 [i, j'] 任意位置开始的最长非重复子串都不可能比 [i, j) 长了，所以滑动窗口直接滑到 j' 开始。
"""


