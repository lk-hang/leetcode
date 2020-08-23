"""
Given two arrays of integers nums and index. Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.

"""
from typing import List
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = [nums[0]]
        for i, idx in enumerate(index[1:]):
            target = target[:idx] + [nums[i+1]] + target[idx:]
        return target