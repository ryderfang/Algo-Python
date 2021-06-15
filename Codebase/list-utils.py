#! /usr/local/bin/python3

from typing import List
from functools import reduce
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

#! reduce
# def permute(self, nums: List[int]) -> List[List[int]]:
#     def reduct_func(a: List[int], b: int):
#         tmp = []
#         print(a, b)
#         for l in a:
#             for i in range(len(l) + 1):
#                 tmp.append(l[:i] + [b] + l[i:])
#         return tmp
#     ans = reduce(reduct_func, nums, [[]])
#     return ans

def sum_list(lst: List[List[int]]):
    return sum(lst, [])

if __name__ == "__main__":
    nums = [1,2,3]

    # enumerate
    for i, v in enumerate(nums):
        print(i, v)
    # filter
    print(list(filter(lambda x: x % 2 != 0, nums)))
    # map
    print(list(map(lambda a: a ** 2, nums)))
    # reduce
    print(reduce(lambda a, b: a * b, nums))
    
    # reverse
    print(nums[::-1])
    # swap
    nums[0], nums[2] = nums[2], nums[0]
    # get min/max of list
    print(min(nums))
    # assign
    nums[1:3] = [0] * 2
    # contact
    tmp = [3,4,5]
    print(nums)
    print([*nums, *tmp]) # nums + tmp

    print(sum_list([[1], [2,3], [4,5,6]]))
    print(distinct_list([1, 1, 2, 3, 4, 4]))
    print(distinct_nested_list([[1], [1, 2], [1, 2], [1, 2, 3]]))