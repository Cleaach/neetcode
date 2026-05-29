class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [False for num in nums]
        permutation = [69 for num in nums]
        res = []
        n = len(nums)
        def backtrack(vis, perm, totalVisited): # total visited so far 3: [x, x, x, 69, 69, ...]
            if totalVisited == n:
                res.append(perm)
            else:
                for i in range(n):
                    if not vis[i]:
                        newVis = vis[:]
                        newVis[i] = True
                        newPerm = perm[:]
                        newPerm[totalVisited] = nums[i]
                        backtrack(newVis, newPerm, totalVisited + 1)
        backtrack(visited, permutation, 0)
        return res