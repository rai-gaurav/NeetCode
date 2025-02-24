# https://neetcode.io/problems/binary-tree-diameter
# The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.
# The length of a path between two nodes in a binary tree is the number of edges between the nodes.
# Given the root of a binary tree root, return the diameter of the tree.
# Input: root = [1,null,2,3,4,5]
# Output: 3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return res
