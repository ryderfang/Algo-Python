#! /usr/local/bin/python3

from typing import List
import itertools

def distinct_nested_list(nested_lst: List[List[int]]):
    # array = set(map(lambda x: tuple(x), array))
    # array = map(lambda x: list(x), array)
    # return list(array)
    return [list(y) for y in set([tuple(x) for x in nested_lst])]

def distinct_list(lst: List[int]):
    return list(set(lst))

def permute(lst: List[int]):
    return [list(x) for x in list(itertools.permutations(lst))]

if __name__ == "__main__":
    # enumerate
    for i, v in enumerate([1, 2]):
        print(i, v)
    
    # get min/max of list
    print(min([1,2,3]))

    # assign
    a = [1, 2, 3]
    a[1:3] = [0] * 2

    print(distinct_list([1, 1, 2, 3, 4, 4]))
    print(distinct_nested_list([[1], [1, 2], [1, 2], [1, 2, 3]]))