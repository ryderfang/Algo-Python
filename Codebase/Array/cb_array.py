#
#
#
from typing import List

def distinct_list(array: List):
    array = map(lambda x: tuple(x), array)
    array = list(set(array))
    array = map(lambda x: list(x), array)
    return list(array)