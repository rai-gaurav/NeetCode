# https://neetcode.io/problems/subtree-of-a-binary-tree
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Input: root = [1,2,3,4,5], subRoot = [2,4,5]
# Output: true

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def sameTree(root1, root2):
            if not root1 and not root2:
                return True
            if root1 and root2 and root1.val == root2.val:
                return (sameTree(root1.left, root2.left) and
                        sameTree(root1.right, root2.right))
            return False

        if sameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
