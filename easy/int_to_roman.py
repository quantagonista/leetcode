class Solution:
    def intToRoman(self, num: int) -> str:
        # units = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        # units_int = [1000, 500, 100, 50, 10, 5, 1]

        units = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        units_int = [1, 5, 10, 50, 100, 500, 1000]

        # units = {
        #     1: 'I',
        #     5: 'V',
        #     10: 'X',
        #     50: 'L',
        #     100: 'C',
        #     500: 'D',
        #     1000: 'M',
        # }
        #
        # exceptions = {
        #     4: 'IV',
        #     9: 'IX',
        #     40: 'XL',
        #     90: 'XC',
        #     400: 'CD',
        #     900: 'CM',
        # }

        power = 1
        div = 10

        r = 0
        res = ''
        ## 78

        while num:
            r = num % div * power

            for i in range(len(units_int) - 1, 0, -1):
                n = units_int[i]

                if r == n:
                    res = units[i] + res
                    break

                if r % n == 0:
                    res = (units[i] * (r // n)) + res
                    break

                if r < n:
                    sub_units = units[:i]
                    for y in range(len(sub_units) - 1, 0, -1):
                        nn = sub_units[y]

                        rr = r % nn


assert Solution().intToRoman(1) == 'I'
assert Solution().intToRoman(10) == 'X'
assert Solution().intToRoman(38) == 'XXXVIII'
assert Solution().intToRoman(92) == 'XCII'
