"""
Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.
"""

class Solution:
    def findComplement(self, num: int) -> int:
        bin_num = bin(num)[2:]
        return int(str(int(len(bin_num) * '1') - int(bin_num)), 2)
