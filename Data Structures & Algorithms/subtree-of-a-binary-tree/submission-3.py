class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        # Check if subRoot matches at current node
        if self.isSameTree(root, subRoot):
            return True
        
        # Recursively check left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, A: Optional[TreeNode], B: Optional[TreeNode]) -> bool:
        if not A and not B:
            return True
        if not A or not B:
            return False
        return (A.val == B.val and 
                self.isSameTree(A.left, B.left) and 
                self.isSameTree(A.right, B.right))