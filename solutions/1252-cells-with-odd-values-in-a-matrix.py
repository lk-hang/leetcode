"""
Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all indices.

"""

from typing import List

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        count_row = [0] * n
        count_col = [0] * m
        for index in indices:
            i, j = index
            count_row[i] += 1
            count_col[j] += 1

        total = 0

        total_r = 0
        for count_r in count_row:
            if count_r % 2 == 1:
                total += m
                total_r += 1

        add_to_total = n - total_r * 2
        for count_c in count_col:
            if count_c % 2 == 1:
                total += add_to_total
        return total