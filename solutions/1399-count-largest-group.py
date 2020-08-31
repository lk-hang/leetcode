"""
Given an integer n. Each number from 1 to n is grouped according to the sum of its digits.

Return how many groups have the largest size.
"""

class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sum_digits(integer):
            tot = 0
            while integer:
                tot += integer % 10
                integer = integer // 10
            return tot

        counter = dict()
        for i in range(1, n + 1):
            tot = sum_digits(i)
            if tot in counter:
                counter[tot] += 1
            else:
                counter[tot] = 1
        largest_group = 1
        count = 0
        for key in counter.keys():
            if counter[key] == largest_group:
                count += 1
            elif counter[key] > largest_group:
                count = 1
                largest_group = counter[key]
        return count
