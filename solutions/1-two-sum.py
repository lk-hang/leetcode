"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
import numpy as np
from typing import List
class Solution:  
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            res = dict()
            # O(N)
            for i, num in enumerate(nums):
                if num not in res:
                    res[num] = i
                else:
                    res[num] = [res[num], i]

            for num, i in res.items():
                if target - num in res:
                    key = res[target - num]
                    if isinstance(key, list):
                        return key
                    elif key == i:
                        continue
                    else:
                        return [i, key]

if __name__ == "__main__":
    sol = Solution()
    solution = sol.twoSum([2, 7, 11, 15], 9)
    print(solution)



