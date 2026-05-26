# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkNode(node, minAllowed, maxAllowed):
            if not node:
                return True
            elif node.val <= minAllowed or node.val >= maxAllowed:
                return False
            return True and checkNode(node.left, minAllowed, min(maxAllowed, node.val)) and checkNode(node.right, max(minAllowed, node.val), maxAllowed)
        return checkNode(root, float('-inf'), float('inf'))