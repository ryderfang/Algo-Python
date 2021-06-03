#! /usr/local/bin/python3

from typing import List

def list_to_str(nums: List[int]):
    return ''.join(str(x) for x in nums)

if __name__ == "__main__":
    print(list_to_str([1, 2, 3]))

    # 左除 0, 左补0
    print("000111".lstrip("0"))
    print("111".rjust(6, "0"))
    # 右除0，右补0
    print("11000".rstrip("0"))
    print("111".ljust(6, "0"))