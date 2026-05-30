class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            split_sum = node.val + max(0, max(left, 0) + max(right, 0))
            res = max(split_sum, res)
            single_sum = node.val + max(0, max(left, right))
            return single_sum

        dfs(root)
        return res