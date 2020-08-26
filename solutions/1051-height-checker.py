"""
Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students that must move in order for all students to be standing in non-decreasing order of height.

Notice that when a group of students is selected they can reorder in any possible way between themselves and the non selected students remain on their seats.
"""

from typing import List
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
#        O(N log N)
        sorted_heights = sorted(heights)
        
        total = 0
        for i, j in zip(heights, sorted_heights):
            if i != j:
                total += 1
        
        return total

