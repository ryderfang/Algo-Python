#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
from itertools import count
from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def _valid(sub):
            sz = len(sub)
            if sz == 0:
                return False
            if sz == 1:
                return True
            if sz == 2:
                return sub[0] != '0'
            if sz == 3:
                if sub[0] == '0' or int(sub[0]) > 2:
                    return False
                tmp = int(sub[0]) * 100 + int(sub[1]) * 10 + int(sub[2])
                return tmp <= 255
            return False
            
        def _dfs(sub, tmp, cnt):
            if cnt == 1:
                if _valid(sub):
                    ans.append('.'.join(tmp + [sub]))
                return
            sz = len(sub)
            for i in range(1, sz - cnt + 2):
                if _valid(sub[0:i]):
                    _dfs(sub[i:], tmp + [sub[0:i]], cnt - 1)

        _dfs(s, [], 4)
        return ans
# @lc code=end

