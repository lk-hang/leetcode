"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
"""


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        perimeter = 0
        col = n * [0]
        for i in range(m):
            row = 0
            for j in range(n):
                if grid[i][j] == 1:
                    if row == 0:
                        perimeter += 1
                        row = 1
                    if col[j] == 0:
                        perimeter += 1
                        col[j] = 1
                else:
                    if row == 1:
                        perimeter += 1
                        row = 0
                    if col[j] == 1:
                        perimeter += 1
                        col[j] = 0
            if row == 1:
                perimeter += 1

        return perimeter + sum (el == 1 for el in col)
