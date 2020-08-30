"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.
"""

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = dict()
        for el in arr2:
            counter[el] = 0

        not_in_arr2  = []
        for el in arr1:
            if el in counter:
                counter[el] += 1
            else:
                not_in_arr2.append(el)

        sol = []
        for el in arr2:
            for _ in range(counter[el]):
                sol.append(el)

        return sol + sorted(not_in_arr2)
