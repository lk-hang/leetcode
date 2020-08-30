"""
Given an integer array arr. You have to sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the sorted array.
"""

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        counter = dict()
        for el in arr:
            num_one = sum(1 for ch in bin(el)[2:] if ch == '1')
            if num_one not in counter:
                counter[num_one] = [el]
            else:
                counter[num_one].append(el)

        sol = []
        for key in sorted(counter.keys()):
            sol += sorted(counter[key])
        return sol
