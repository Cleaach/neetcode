# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def bfs(node, height):
            if not node:
                return
            if len(res) < height + 1:
                res.append([])
            res[height].append(node.val)
            bfs(node.left, height + 1)
            bfs(node.right, height + 1)

        bfs(root, 0)

        return res