from typing import List


def duplicateZeros(arr: List[int]) -> None:
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            for j in range(len(arr) - 1, i, -1):
                arr[j] = arr[j - 1]
            i += 1
        i += 1

    print(arr)


duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0])
duplicateZeros([1, 0, 0, 2, 0, 3])
duplicateZeros([1, 0, 2, 0, 3])
duplicateZeros([1, 0, 2, 3])
duplicateZeros([1, 2, 3])
