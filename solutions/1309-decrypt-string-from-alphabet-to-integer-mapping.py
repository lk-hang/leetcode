"""
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.
"""

class Solution:
    def freqAlphabets(self, s: str) -> str:
        letters = list('abcdefghijklmnopqrstuvwxyz')

        count = 1
        idx_in_str = ""
        sol = ""
        while s != "":
            popped = s[-1]
            s = s[:-1]
            if popped == '#':
                count = 2
            else:
                count -= 1
                idx_in_str = popped + idx_in_str
                if count == 0:
                    sol = letters[int(idx_in_str) - 1] + sol
                    count = 1
                    idx_in_str = ""

        return sol