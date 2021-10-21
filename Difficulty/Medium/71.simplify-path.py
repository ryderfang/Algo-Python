#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        sz = len(path)
        stack = []
        i = 0
        while i < sz:
            temp = ''
            i += 1
            while i < sz and path[i] != '/':
                temp += path[i]
                i += 1
            if temp == '..':
                if len(stack) > 0:
                    stack.pop()
            elif temp == '.' or temp == '':
                pass
            else:
                stack.append(temp)
        ret = ''
        for x in stack:
            ret += '/'
            ret += x
        ret = '/' if len(ret) == 0 else ret
        return ret
# @lc code=end

