"""
Given an array of unique integers salary where salary[i] is the salary of the employee i.

Return the average salary of employees excluding the minimum and maximum salary.
"""

class Solution:
    def average(self, salary: List[int]) -> float:
        min_val = 9e9
        max_val = -1
        tot = 0
        count = 0
        for el in salary:
            count += 1
            tot += el
            min_val = min(min_val, el)
            max_val = max(max_val, el)

        return (tot - min_val - max_val) / (count - 2)
