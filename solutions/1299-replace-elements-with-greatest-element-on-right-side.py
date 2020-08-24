"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
"""

from typing import List
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # inplace
        # n = len(arr)
        # max_el = -1
        # for i in range(n - 1, -1 , -1):
        #     el = arr[i]
        #     arr[i] = max_el
        #     max_el = max(max_el, el)
        # return arr

        # return new object
        sol = []
        max_el = -1
        for el in arr[::-1]:
            sol.append(max_el)
            max_el = max(max_el, el)
        return sol[::-1]