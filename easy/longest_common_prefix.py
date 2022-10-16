from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ''
        i = 0

        while True:
            sub_set = set()

            for str_ in strs:
                try:
                    sub_set.add(str_[i])

                except IndexError:
                    return pref

            if len(sub_set) == 1:
                pref += sub_set.pop()
                i += 1
            else:
                return pref


assert Solution().longestCommonPrefix(['abcd', 'abcdef', 'abc']) == 'abc'
assert Solution().longestCommonPrefix(['abcd', 'abcdef', '']) == ''