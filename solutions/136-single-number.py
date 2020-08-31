"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sol = set()
        for el in nums:
            if el not in sol:
                sol.add(el)
            else:
                sol.remove(el)

        return sol.pop()

