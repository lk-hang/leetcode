"""
Given an integer n, return any array containing n unique integers such that they add up to 0.
"""

from typing import List
class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        total = 0
        sol = []
        for i in range(n - 1):
            sol.append(i)
            total += i

        sol.append(-total)
        return sol