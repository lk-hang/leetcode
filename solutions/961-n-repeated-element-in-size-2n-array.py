"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.
"""
from typing import List
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        seen = set()
        for el in A:
            if el not in seen:
                seen.add(el)
            else:
                return el