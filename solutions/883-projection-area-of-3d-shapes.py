"""
On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Now we view the projection of these cubes onto the xy, yz, and zx planes.

A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane.

Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return the total area of all three projections.


 """

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        surface = 0
        max_col = [0] * n
        max_row = [0] * n
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0:
                    surface += 1
                    max_row[i] = max(max_row[i], grid[i][j])
                    max_col[j] = max(max_col[j], grid[i][j])

        return sum(max_col) + sum(max_row) + surface
