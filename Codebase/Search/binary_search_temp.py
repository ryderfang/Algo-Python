#! /usr/local/bin/python3

from typing import List
import bisect

# 返回第一个找到的值
def bsearch1_i(a: List[int], x: int, l: int = 0, r: int = None) -> int:
    r = r or len(a) - 1
    while l <= r:
        m = l + (r - l) // 2
        if a[m] < x:
            l = m + 1
        elif a[m] > x:
            r = m - 1
        else:
            return m
    return -1

def bsearch1_b(a: List[int], x: int, l: int = 0, r: int = None) -> int:
    r = r or len(a) - 1
    while l <= r:
        m = l + (r - l) // 2
        if a[m] < x:
            l = m + 1
        elif a[m] > x:
            r = m - 1
        else:
            return True
    return False

# 递归
def bsearch2(a: List[int], x: int, l: int = 0, r: int = None) -> int:
    r = r or len(a)
    if l > r:
        return -1
    m = l + (r - l) // 2
    if a[m] < x:
        bsearch2(a, m + 1, r, x)
    elif a[m] > x:
        bsearch2(a, l, m - 1, x)
    else:
        return m

# 返回 index 最小的 (wiki 实现)
def bsearch_leftmost(a: List[int], x: int, l: int = 0, r: int = None) -> int:
    r = r or len(a)
    while l < r:
        m = l + (r - l) // 2
        if a[m] < x:
            l = m + 1
        else:
            # 相等也要更新上边界
            r = m
    return l

# 返回 index 最大的 (wiki 实现)
def bsearch_rightmost(a: List[int], x: int, l: int = 0, r: int = None) -> int:
    r = r or len(a)
    while l < r:
        m = l + (r - l) // 2
        if a[m] <= x:
            # 相等更新下边界
            l = m + 1
        else:
            r = m
    # 这里注意 -1
    return r - 1


if __name__ == "__main__":
    print(bsearch1_i([1,2,4,4,4,5,6,7], 4))        # 3
    print(bsearch1_b([1,2,4,4,4,5,6,7], 8))        # False
    print(bsearch2([1,2,4,4,4,5,6,7], 4, 0, 8))    # 4

    print(bsearch_leftmost([1,2,4,4,4,5,6,7], 8))  # 8
    print(bsearch_rightmost([1,2,4,4,4,5,6,7], 3)) # 1

    # Return the index where to insert item x in list a, assuming a is sorted.
    # The return value i is such that all e in a[:i] have e < x, and all e in
    # a[i:] have e >= x. So if x already appears in the list, i points just before the leftmost x already there.
    print(bisect.bisect_left([1,2,4,4,4,5,6,7],8))  # 8
    # bisect == bisect_right
    # 这个返回是插入位，即 rightIndex + 1 的位置
    print(bisect.bisect([1,2,4,4,4,5,6,7], 8))       # 8
    print(bisect.bisect_right([1,2,4,4,4,5,6,7], 3)) # 2
