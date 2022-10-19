class Solution:
    def comp(self, l):
        try:
            return l[-1] - l[0]
        except:
            return -1

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        m = {}
        for i, c in enumerate(s):
            if c not in m:
                m[c] = [i]
                continue
            m[c].append(i)
        n = sorted(m.values(), key=lambda v: self.comp(v), reverse=True)
        i = n[0]
        if len(i) > 1:
            return len(s[i[0] + 1: i[-1]])
        return -1

assert Solution().maxLengthBetweenEqualCharacters('aa') == 0
assert Solution().maxLengthBetweenEqualCharacters('abca') == 2
assert Solution().maxLengthBetweenEqualCharacters('abcy') == -1
assert Solution().maxLengthBetweenEqualCharacters('abcacbna') == 6

