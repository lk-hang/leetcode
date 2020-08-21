"""
Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

"""

from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        n = len(indices)       
        new_string = ' ' * n
        for i, index in enumerate(indices):
            new_string = new_string[:index] + s[i] + new_string[index+1:]
        return new_string