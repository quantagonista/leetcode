class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False

        s1 = []
        m = {
            '}': '{',
            ')': '(',
            ']': '[',
        }

        for c in s:
            if c in {'{', '(', '['}:
                s1.append(c)
            elif c in {'}', ')', ']'}:
                last = s1.pop()
                try:
                    if last != m.get(c):
                        return False
                except IndexError:
                    return False

        if len(s1):
            return False

        return True


assert Solution().isValid('{}') == True
assert Solution().isValid('{}()') == True
assert Solution().isValid('(([{}]))') == True
assert Solution().isValid('') == False
assert Solution().isValid('(') == False
assert Solution().isValid('({)') == False
assert Solution().isValid('(]') == False
