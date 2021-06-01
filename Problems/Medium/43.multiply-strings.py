#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
from typing import List
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        sz1 = len(num1)
        sz2 = len(num2)
        ans = [0] * (sz1 + sz2 + 1)
        # reversed
        def foo(num: str, digit: int, offset: int) -> List[int]:
            ret = [0] * offset
            carry = 0
            for x in num[::-1]:
                tmp = int(x) * digit + carry
                ret.append(tmp % 10)
                carry = tmp // 10
            ret.append(carry)
            return ret
        def add(list1: List[int], list2: List[int]):
            sz1 = len(list1)
            sz2 = len(list2)
            sz = max(sz1, sz2)
            list1 += [0] * (sz - sz1 + 1)
            list2 += [0] * (sz - sz2 + 1)
            carry = 0
            for i in range(sz+1):
                tmp = list1[i] + list2[i] + carry
                list1[i] = tmp % 10
                carry = tmp // 10

        for i in range(sz2):
            tmp = foo(num1, int(num2[sz2-1-i]), i)
            add(ans, tmp)
        ret = ''.join(str(x) for x in reversed(ans))
        ret = ret.lstrip("0")
        # 0 * 0
        if ret == '':
            ret = '0'
        return ret

# @lc code=end

