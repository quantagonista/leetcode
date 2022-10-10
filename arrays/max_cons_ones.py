from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    max_cons = 0
    curr = 0
    for num in nums:
        if num == 0:
            if curr > max_cons:
                max_cons = curr
            curr = 0

        else:
            curr += 1

    if curr > max_cons:
        max_cons = curr
    return max_cons


assert 0 == findMaxConsecutiveOnes([0, 0])
assert 1 == findMaxConsecutiveOnes([0, 1, 0])
assert 2 == findMaxConsecutiveOnes([0, 1, 0, 1, 1, 0])
assert 3 == findMaxConsecutiveOnes([0, 1, 0, 1, 1, 0, 1, 1, 1, 0])
assert 3 == findMaxConsecutiveOnes([0, 1, 0, 1, 1, 0, 1, 1, 1])
