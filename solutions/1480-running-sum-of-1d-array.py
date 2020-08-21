"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""
from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        el = 0
        sol = []
        for num in nums:
            el += num
            sol.append(el)
        return sol