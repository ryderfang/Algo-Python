#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def addBracket(now: str, left: int, right: int):
            nonlocal ans
            if len(now) == 2 * n:
                ans.append(now)
                return
            if left > 0:
                addBracket(now + '(', left - 1, right)
            if len(now) > 0 and right > 0 and left < right:
                addBracket(now + ')', left, right - 1) 
        
        addBracket('', n, n)
        return ans

# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.generateParenthesis(1))
#     print(sol.generateParenthesis(2))
#     print(sol.generateParenthesis(3))
#     print(sol.generateParenthesis(4))
#     print(sol.generateParenthesis(5))
#     print(sol.generateParenthesis(6))
#     print(sol.generateParenthesis(7))
#     print(sol.generateParenthesis(8))
# @lc code=end

