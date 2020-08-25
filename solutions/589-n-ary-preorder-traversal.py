"""
Given an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

from typing import List
class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        # recursive
        sol = []
        if root is not None:
            sol.append(root.val)
            for child in root.children:
                sol += self.preorder(child)
        return sol

        # iterative
