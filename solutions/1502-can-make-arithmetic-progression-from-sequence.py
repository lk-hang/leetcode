"""
Given an array of numbers arr. A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.
"""
from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        min_el = min(arr)

        x = (max(arr) - min_el) / (n - 1)
        return sum(arr) == n * (min_el - x + (n + 1) / 2 * x)