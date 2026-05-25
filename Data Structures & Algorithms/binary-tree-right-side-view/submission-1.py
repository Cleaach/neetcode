# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []

        def bfs(node, height):
            if not node:
                return
            if len(res) < height + 1:
                res.append(0)
            res[height] = node.val
            bfs(node.left, height + 1)
            bfs(node.right, height + 1)
        
        bfs(root, 0)
        return res