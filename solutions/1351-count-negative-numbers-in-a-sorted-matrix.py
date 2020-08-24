"""
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.

Return the number of negative numbers in grid.
"""
from typing import List
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        sol = 0
        memory_col = n
        for row_idx in range(m):
            row = grid[row_idx]
            for col_idx in range(memory_col):
                if row[col_idx] < 0:
                    sol += (memory_col - col_idx) * (m - row_idx)
                    memory_col = col_idx
                    break
            if memory_col == 0:
                break
        return sol