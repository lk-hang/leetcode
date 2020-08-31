"""
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
"""

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])

        for col in range(n):
            check, row = matrix[0][col], 1
            while col + row < n and row < m:
                if matrix[row][col + row] != check:
                    return False
                row += 1

        for row in range(1, m):
            check, col = matrix[row][0], 1
            while col + row < m and col < n:
                if matrix[row + col][col] != check:
                    return False
                col += 1

        return True
