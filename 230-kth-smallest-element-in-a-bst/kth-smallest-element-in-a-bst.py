# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: 'TreeNode', k: int) -> int:
        stack = []
        
        while True:
            # Go to the leftmost node
            while root:
                stack.append(root)
                root = root.left
            
            # Process node
            root = stack.pop()
            k -= 1
            
            if k == 0:
                return root.val
            
            # Move to right subtree
            root = root.right