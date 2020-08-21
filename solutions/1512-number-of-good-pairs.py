"""
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.
"""

from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        def sum_to_N(n):
            if n == 1:
                return 0
            sol = 0
            i = 1
            while i < n:
                sol += i
                i += 1
            return sol
        
        counter = dict()
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1

        sol = 0
        for val in counter.values():
            sol += sum_to_N(val)
    
        return sol