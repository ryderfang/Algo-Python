#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def __init__(self):
        self.ans = 1
        self.beg = self.end = 0
    
    def checkPalindrome(self, s: str, p: int, q: int):
        sz = len(s)
        if p >= 0 and q < sz and self.dp[p][q]:
            return
        while p >= 0 and q < sz:
            if s[p] == s[q]:
                self.dp[p][q] = 1
                if q - p + 1 > self.ans:
                    self.ans = q - p + 1
                    self.beg = p
                    self.end = q
                p -= 1
                q += 1
            else:
                break

    def longestPalindrome(self, s: str) -> str:
        sz = len(s)
        self.dp = [[0 for i in range(sz)] for j in range(sz)]
        for i in range(sz):
            # [i-1, i]
            self.checkPalindrome(s, i - 1, i)
            # [i, i+1]
            self.checkPalindrome(s, i, i + 1)
            # [i-1, i+1]
            self.checkPalindrome(s, i - 1, i + 1)
        print(self.ans)
        result = s[self.beg:self.end+1]
        return result

# @lc code=end

