"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        max_num = max(x, y)
        binary = 1
        while max_num > binary:
            binary <<= 1


        count = 0
        while binary > 0:
            if x // binary != y // binary:
                count += 1
            x %= binary
            y %= binary
            binary >>= 1
        return count
