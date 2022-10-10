from typing import List


def findNumbers(nums: List[int]) -> int:
    return sum([1 for num in nums if not len(str(num)) % 2])



assert 0 == findNumbers([1,2,3])
assert 1 == findNumbers([1,22,3])
assert 2 == findNumbers([1,22,3456])
