"""
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
"""

class Solution:
    def maximum69Number (self, num: int) -> int:
        base = 1
        while num > base:
            base *= 10
        base = base // 10

        sol = 0
        while num > 0:
            div = num // base
            if div == 6:
                sol += 9 * base + num % base
                return sol
            else:
                sol += 9 * base
                num = num % base
                base = base // 10
        return sol

        # num_in_str = str(num)
        # for i, el in enumerate(num_in_str):
        #     if el == '6':
        #         return int(num_in_str[:i] + '9' + num_in_str[i+1:])
        # return num




