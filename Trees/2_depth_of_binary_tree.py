# https://neetcode.io/problems/depth-of-binary-tree
# Given the root of a binary tree, return its depth.
# The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.
  
# Input: root = [1,2,3,null,null,4]
# Output: 3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
