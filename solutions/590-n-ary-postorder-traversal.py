"""
Given an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from typing import List
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # recursive
        if root is None:
            return []
        sol = []
        for child in root.children:
            sol += self.postorder(child)
        sol.append(root.val)
        return sol

        # iterative (not sure how to do this)