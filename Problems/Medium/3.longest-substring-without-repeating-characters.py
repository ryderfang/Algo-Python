#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        f = []
        sz = len(s)
        for i in range(sz):
            idx = s[i+1:].find(s[i])
            f.append(idx + i + 1 if idx >= 0 else sz)
        result = 1
        longest_i = 0
        longest_j = 1
        for i in range(sz):
            j = i
            k = f[i]
            while j < sz:
                k = min(k, f[j])
                if j >= k:
                    break
                j += 1
            if result < k - i:
                result = k - i
                longest_i = i
                longest_j = k
        #print('from: <' + str(longest_i) + '> to: <' + str(longest_j) + '>')
        return result
# @lc code=end

