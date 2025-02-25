# https://neetcode.io/problems/balanced-binary-tree
# Given a binary tree, return true if it is height-balanced and false otherwise.
# A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Input: root = [1,2,3,null,null,4]
# Output: true

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True

        def dfs(root):
            nonlocal isBalanced
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left < 0 or right < 0 or abs(left - right) > 1:
                isBalanced = False
            return 1 + max(left, right)

        dfs(root)
        return isBalanced
