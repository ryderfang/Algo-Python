#! /usr/local/bin/python3

from typing import List

def quick_sort(b: int, e: int, a: List[int]):
    i, j, x = b, e, a[(b + e) // 2]
    while True:
        while a[i] < x:
            i += 1
        while a[j] > x:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
        if i >= j:
            break
    if i < e:
        quick_sort(i, e, a)
    if j > b:
        quick_sort(b, j, a)

if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 5, 0],
        [10, 3, 2, 2, 0, 1],
    ]
    for x in test_cases:
        quick_sort(0, len(x) - 1, x)
        print(x)