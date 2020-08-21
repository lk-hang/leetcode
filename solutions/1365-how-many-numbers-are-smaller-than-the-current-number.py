"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
"""

from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        # O(N)
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
        
        solution = []
        for num in nums:
            num_smaller = 0
            for el in counter:
                if num > el:
                    num_smaller += counter[el]
            solution.append(num_smaller)
        
        return solution
        