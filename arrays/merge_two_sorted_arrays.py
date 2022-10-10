import copy
from typing import List


# [1, 3, 5, 0, 0] +  [-2, 3] = [-2, 1, 3, 3, 5, 3]
# [1, 3, 5, 0]    +  [2]     = [1 , 3, 5, 2]
# [-1, 3, 5, 0]   +  [-2]    = [-2 , -1, 3, 5]

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        f_i = 0
        s_i = 0

        if n == 0:
            return

        if n == 1:
            nums1[0] = nums2[0]
            return

        while s_i < n:
            f_item = nums1[f_i]
            s_item = nums2[s_i]

            if s_item <= f_item:
                for i in range(len(nums1) - 1, f_i, -1):
                    nums1[i], nums1[i - 1] = nums1[i - 1], nums1[i]

                nums1[f_i] = s_item
                f_i += 1
                s_i += 1

            else:
                # for i in range(len(nums1) - 1, f_i + 1, -1):
                #     nums1[i], nums1[i - 1] = nums1[i - 1], nums1[i]
                #
                # nums1[f_i + 1] = s_item
                f_i += 1




def test(a, la, b, lb, c):
    f = copy.copy(a)
    s = copy.copy(b)

    Solution().merge(f, la, s, lb)

    for i in range(len(f)):
        assert f[i] == c[i]


test([1], 1, [], 0, [1])
test([0], 0, [1], 1, [1])
test([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6])
test([-1, 2, 3, 4, 0, 0], 3, [1, 3], 2, [-1, 1, 2, 3, 3, 4])
