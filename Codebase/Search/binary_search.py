#! /usr/local/bin/python3

from typing import List
import bisect

### --- 模板 --- ###
def _bsearch(a: List[int], x: int, l: int = 0, r: int = None) -> int:
    r = r or len(a)
    while l < r:
        m = l + (r - l) // 2
        if a[m] < x:
            l = m + 1
        else:
            r = m
    return l

def _exists(a: List[int], x: int) -> bool:
    idx = _bsearch(a, x)
    return idx >= 0 and idx < len(a) and a[idx] == x

### --- 模板 --- ###

if __name__ == "__main__":
    print(_bsearch([1,2,4], 5))             # 3
    print(_bsearch([1,2,4], -1))            # 0

    print(_bsearch([1,2,4,4,4,5,6,7], 4))   # 2
    print(_bsearch([1,2,4,4,4,5,6,7], 1))   # 0 
    print(_bsearch([1,2,4,4,4,5,6,7], 0))   # 0
    print(_bsearch([1,2,4,4,4,5,6,7], 8))   # 8
    print(_exists([1,2,4,4,4,5,6,7], 10))   # False