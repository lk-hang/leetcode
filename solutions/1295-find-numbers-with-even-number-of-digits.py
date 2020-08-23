"""
Given an array nums of integers, return how many of them contain an even number of digits.
"""
from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:

#         def count_digit(n):
#             if n < 10:
#                 return 1
#             else:
#                 return 1 + count_digit(n // 10)

#         sol = 0
#         for num in nums:
#             if count_digit(num) % 2 == 0:
#                 sol += 1
#         return sol

        sol = 0
        for num in nums:
            two_digit = num // 10
            four_digit = num // 1000
            six_digit = num // 100000
            if (0 < two_digit < 10) or (0 < four_digit < 10) or (0 < six_digit < 10):
                sol += 1
        return sol
