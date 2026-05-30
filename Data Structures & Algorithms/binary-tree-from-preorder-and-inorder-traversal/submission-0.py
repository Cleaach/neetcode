# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        n = len(preorder)
        
        # get root, 1st in preorder
        r = preorder[0]
        root = TreeNode(r)

        # count how many nodes are in left and right subtrees via inorder
        c = 0
        for i in range(n):
            if inorder[i] == r:
                c = i

        # partition the remainder of preorder and inorder based on c
        # e.g. pre = [1,2,3,4], in = [2,1,3,4], c = 1
        leftpreorder = preorder[1:1 + c]
        leftinorder = inorder[0:c]
        rightpreorder = preorder[1 + c:]
        rightinorder = inorder[1 + c:]
    
        root.left = self.buildTree(leftpreorder, leftinorder)
        root.right = self.buildTree(rightpreorder, rightinorder)

        return root