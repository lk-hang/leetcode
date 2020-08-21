"""
We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list.
"""

from typing import List
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        lsts = []
        n = len(nums) // 2
        for i in range(n):
            lsts += nums[i*2] * [nums[i*2+1]]
        return lsts