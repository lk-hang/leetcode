"""
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
"""



class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr.sort()
        n = len(arr)
        sol = [arr[0:2]]

        min_diff = arr[1] - arr[0]
        for i in range(2, n):
            prev, curr = arr[i-1:i+1]
            diff = curr - prev
            if diff < min_diff:
                sol = [[prev, curr]]
                min_diff = diff
            elif diff == min_diff:
                sol.append([prev, curr])
        return sol
