# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        
        def getHeight(node):
            nonlocal balanced
            
            if not node:
                return 0
            
            left = getHeight(node.left)
            right = getHeight(node.right)

            if abs(left - right) > 1:
                balanced = False

            return 1 + max(left, right)

        getHeight(root)
        return balanced