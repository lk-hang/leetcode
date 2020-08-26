"""
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.
"""
from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = dict()
        for el in arr:
            if el not in counter:
                counter[el] = 1
            else:
                counter[el] += 1
        
        
        unique = set()
        for val in counter.values():
            if val not in unique:
                unique.add(val)
            else:
                return False
        return True
