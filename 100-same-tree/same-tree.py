# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: 'TreeNode', q: 'TreeNode') -> bool:
        # If both are null
        if not p and not q:
            return True
        
        # If one is null or values differ
        if not p or not q or p.val != q.val:
            return False
        
        # Recursively check left and right
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))