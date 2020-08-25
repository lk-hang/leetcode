"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
"""
from typing import List

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        stack = []
        while A and A[0] <= 0:
            stack.append(A.pop(0))


        sol = []
        while stack or A:
            if not stack:
                el = A.pop(0)
            elif not A:
                el = stack.pop()
            else:
                if (- stack[-1]) < A[0]:
                    el = stack.pop()
                else:
                    el = A.pop(0)

            sol.append(el * el)
        return sol