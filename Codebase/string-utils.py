#! /usr/local/bin/python3

from typing import List

def list_to_str(nums: List[int]):
    return ''.join(str(x) for x in nums)

if __name__ == "__main__":
    print(list_to_str([1, 2, 3]))