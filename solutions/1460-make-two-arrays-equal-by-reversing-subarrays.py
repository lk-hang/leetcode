"""
Given two integer arrays of equal length target and arr.

In one step, you can select any non-empty sub-array of arr and reverse it. You are allowed to make any number of steps.

Return True if you can make arr equal to target, or False otherwise.

"""
from typing import List
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        counter = {}
        for el in target:
            if el not in counter:
                counter[el] = 1
            else:
                counter[el] += 1

        for el in arr:
            if el not in counter:
                return False
            else:
                counter[el] -= 1
                if counter[el] < 0:
                    return False
        return True
