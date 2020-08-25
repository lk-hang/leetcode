from typing import List

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        # O(N)
        i = 0
        curr_el = A[0]
        for el in A[1:]:
            if curr_el > el:
                return i
            curr_el = el
            i += 1

        # O(Log N)
