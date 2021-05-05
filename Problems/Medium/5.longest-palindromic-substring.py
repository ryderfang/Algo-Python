#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def expandAroundCenter(self, s: str, left: int, right: int):
        sz = len(s)
        while left >= 0 and right < sz and s[left] == s[right]:
            left -= 1
            right += 1
        # 这里长度计算要注意，left--和right++之后才计算的
        return (right - left - 1)

    def longestPalindrome(self, s: str) -> str:
        sz = len(s)
        beg = end = 0
        for i in range(sz):
            # 以 i 为中心的奇回文串
            len1 = self.expandAroundCenter(s, i, i)
            # 以 i,i+1 为中心的偶回文串
            len2 = self.expandAroundCenter(s, i, i + 1)
            length = max(len1, len2)
            if length > end - beg:
                beg = i - (length - 1) // 2
                end = i + length // 2
        result = s[beg:end+1]
        return result

# @lc code=end

