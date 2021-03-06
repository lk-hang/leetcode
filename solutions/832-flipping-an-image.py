"""
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].
"""
from typing import List
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        sol = []
        for row in A:
            new_row = []
            for col in row[::-1]:
                new_row.append(1 - col)
            sol.append(new_row)
        return sol
