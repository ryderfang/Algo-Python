#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
           return [] 
        mp = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        lst = self.letterCombinations(digits[1:])
        ans = []
        prefix = mp[int(digits[0]) - 2]
        if len(lst) > 0:
            for ch in prefix:
                for x in lst:
                    ans.append(ch+x)
        else:
            for ch in prefix:
                ans.append(ch)
        return ans
# @lc code=endg
