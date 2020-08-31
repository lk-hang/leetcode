"""
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.
"""

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        running_sum = 0
        min_val = 9e99
        for num in nums:
            running_sum += num
            min_val = min(min_val, running_sum)

        return max(-min_val + 1 , 1)
