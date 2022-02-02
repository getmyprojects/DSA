"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Leetcode 98
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):

        def valid(node, min_key, max_key):
            if node is None:
                return True

            if node.val <= min_key or node.val >= max_key:
                return False

            return valid(node.left, min_key, node.val) and valid(node.right,
                                                                 node.val,
                                                                 max_key)

        return valid(root, float('-inf'), float('inf'))
