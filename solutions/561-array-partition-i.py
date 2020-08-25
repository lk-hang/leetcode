"""
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
"""
from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        def merge_sort(arr):

            n = len(arr)
            if n <= 1:
                return arr

            left = merge_sort(arr[:n//2])
            right = merge_sort(arr[n // 2:])

            sol = []
            # merge
            for i in range(n):
                if (len(left) == 0) or (right and (left[0] >= right[0])):
                    sol.append(right.pop(0))
                else:
                    sol.append(left.pop(0))
            return sol

        nums = merge_sort(nums)

        return sum(el for i, el in enumerate(nums) if i % 2 == 0)