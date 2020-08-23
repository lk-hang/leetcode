"""
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
"""
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # (a - c) * (b - c) = ab - (a + b) + 1
        great = 0
        greatest = 0
        for num in nums:
            if num > greatest:
                great = greatest
                greatest = num
            elif num > great:
                great = num

        return (greatest - 1) * (great - 1)