"""
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.
"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None:
            return True

        val = root.val
        sol = True
        if root.left:
            sol &= val == root.left.val
            sol &= self.isUnivalTree(root.left)
        if root.right:
            sol &= val == root.right.val
            sol &= self.isUnivalTree(root.right)
        return sol


