"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
"""
from typing import List
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        sol = []
        for i in range(left, right + 1):
            digits = map(int, str(i))

            add = True
            for digit in digits:
                if not digit or i % digit != 0:
                    add = False
                    break

            if add:
                sol.append(i)

        # sol = [i for i in range(left, right + 1) if all(digit and i % digit == 0 for digit in map(int, str(i)))]
        return sol
