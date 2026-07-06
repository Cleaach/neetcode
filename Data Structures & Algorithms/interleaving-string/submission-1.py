class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        a, b = len(s1), len(s2)
        # Allocate (a + 1) x (b + 1) so dp[a][b] is valid
        dp = [[None for _ in range(b + 1)] for _ in range(a + 1)]
        
        def help(i, j):
            # Base Case: Both strings are fully traversed
            if i == a and j == b:
                return True
            
            # Return cached result if already computed
            if dp[i][j] is not None:
                return dp[i][j]
            
            ans = False
            # Option 1: Try matching the next character from s1
            if i < a and s1[i] == s3[i + j]:
                ans = ans or help(i + 1, j)
            
            # Option 2: Try matching the next character from s2
            if j < b and s2[j] == s3[i + j]:
                ans = ans or help(i, j + 1)
            
            dp[i][j] = ans
            return ans
            
        return help(0, 0)