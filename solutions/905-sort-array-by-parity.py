"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.
"""


from typing import List
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        # new object
        # even = []
        # odd = []
        # for el in A:
        #     if el & 1 == 0:
        #         even.append(el)
        #     else:
        #         odd.append(el)
        # return even + odd

        # inplace
        n = len(A)
        curr_idx, pointer = 0, n - 1
        for _ in range(n):
            if A[curr_idx] & 1 == 1:
                A[curr_idx], A[pointer] = A[pointer], A[curr_idx]
                pointer -= 1
            else:
                curr_idx += 1
        return A