#! /usr/local/bin/python3

from typing import List

def distinct_nested_list(array: List[List[int]]):
    array = map(lambda x: tuple(x), array)
    array = list(set(array))
    array = map(lambda x: list(x), array)
    return list(array)

def distinct_list(nums: List[int]):
    return list(set(nums))

if __name__ == "__main__":
    # enumerate
    for i, v in enumerate([1, 2]):
        print(i, v)

    print(distinct_list([1, 1, 2, 3, 4, 4]))
    print(distinct_nested_list([[1], [1, 2], [1, 2], [1, 2, 3]]))