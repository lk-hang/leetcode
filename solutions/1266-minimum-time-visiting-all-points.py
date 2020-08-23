"""
On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.

You can move according to the next rules:

In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
You have to visit the points in the same order as they appear in the array.
"""

from typing import List
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        n = len(points)
        for i in range(n - 1):
            point_now, point_next = points[i : i + 2]
            total_time += max(abs(point_now[0] - point_next[0]), abs(point_now[1] - point_next[1]))
        return total_time