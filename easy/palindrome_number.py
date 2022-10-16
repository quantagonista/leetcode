class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        if len(y) == 1:
            return False

        start = 0
        end = len(y) - 1
        while True:
            if start >= end:
                break

            if y[start] != y[end]:
                return False

            start += 1
            end -= 1

        return True


assert Solution().isPalindrome(0) == False
assert Solution().isPalindrome(121) == True
assert Solution().isPalindrome(1221) == True
assert Solution().isPalindrome(12021) == True
assert Solution().isPalindrome(-121) == False
