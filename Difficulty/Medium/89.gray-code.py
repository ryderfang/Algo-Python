#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
from typing import List
class Solution:
    def grayCode(self, n: int) -> List[int]:
        # 000 001 011 010 110 111 101 100
        def genNext(x, p):
            t = x >> p
            if t & 1:
                return x - 2 ** p
            else:
                return x + 2 ** p
        mp = { 0 }
        arr = [ 0 ]
        sz = 2 ** n
        def dfs(i):
            if len(arr) == sz:
                return True
            find = False
            for j in range(n):
                tmp = genNext(arr[i], j)
                if not (tmp in mp):
                    mp.add(tmp)
                    arr.append(tmp)
                    if dfs(i + 1):
                        find = True
                        break
            if find:
                return True
            else:
                mp.discard(arr[i])
                arr.pop()
                return False
        dfs(0)
        return arr

# @lc code=end

