"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
"""

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        if n < 10:
            return 0
        
        running_prod = 1
        running_sum = 0
        while n > 0:
            rest = n % 10
            running_prod *= rest
            running_sum += rest
            n = n // 10
        
        return running_prod - running_sum
        