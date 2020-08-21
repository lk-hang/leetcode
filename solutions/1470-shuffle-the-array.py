""" 
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""

from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        solution = []
        for i in range(n):
            solution.append(nums[i])
            solution.append(nums[i+n])
        return 