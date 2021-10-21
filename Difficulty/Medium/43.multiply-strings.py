#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
from typing import List

RR_INF = 10000
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #  变成万进制
        def make_ten_thousand_list(nums: str):
            factor = 1
            s = 0
            tmp = []
            for x in reversed(nums):
                s += factor * int(x)
                factor *= 10
                if factor == RR_INF:
                    tmp.append(s)
                    factor = 1
                    s = 0
            tmp.append(s)
            return tmp

        tmp1 = make_ten_thousand_list(num1)
        tmp2 = make_ten_thousand_list(num2)

        # multiply
        def foo(nums: List[int], digit: int, offset: int) -> List[int]:
            ret = [0] * offset
            carry = 0
            for x in nums:
                tmp = x * digit + carry
                ret.append(tmp % RR_INF)
                carry = tmp // RR_INF
            ret.append(carry)
            return ret
        
        # dislocation add
        def add(list1: List[int], list2: List[int]):
            sz1 = len(list1)
            sz2 = len(list2)
            sz = max(sz1, sz2)
            list1 += [0] * (sz - sz1 + 1)
            list2 += [0] * (sz - sz2 + 1)
            carry = 0
            # opt: sz + 1
            for i in range(sz + 1):
                tmp = list1[i] + list2[i] + carry
                list1[i] = tmp % RR_INF
                carry = tmp // RR_INF

        ans = [0] * (len(tmp1) + len(tmp2) + 1)
        for i, v in enumerate(tmp2):
            tmp = foo(tmp1, v, i)
            add(ans, tmp)
        # rjust 左补0，必须
        ret = ''.join(str(x).rjust(4, "0") for x in reversed(ans))
        # remove ahead 0
        ret = ret.lstrip("0")
        # 0 * 0
        if ret == '':
            ret = '0'
        return ret

# @lc code=end

