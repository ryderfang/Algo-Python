#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for i,s in enumerate(strs):
            tmp = ''.join(sorted(s))
            if tmp in ans:
                ans[tmp].append(s)
            else:
                ans[tmp] = [s]
        return list(ans.values())

        
# @lc code=end

