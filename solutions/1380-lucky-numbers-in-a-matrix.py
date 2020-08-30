"""
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
"""
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        sol = []

        memory = n * [0] # num of cols
        max_val = n * [0]
        for row in matrix:
            min_idx = -1
            min_val =  1e8
            for j, col in enumerate(row):
                max_val[j] = max(max_val[j], col)
                if col < min_val:
                    min_idx = j
                    min_val = col
                if col > memory[j]:
                    memory[j] = 0

            if min_val >= max_val[min_idx]:
                memory[min_idx] = max(min_val, memory[min_idx])

