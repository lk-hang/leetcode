"""
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]
"""
from typing import List
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        n = len(S)
        btm, top = 0, n
        solution = [0] * (n + 1)
        for i in range(n):
            if S[i] == 'I':
                solution[i] = btm
                btm += 1
            else:
                solution[i] = top
                top -= 1
        solution[n] = btm
        return solution