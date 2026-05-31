class Solution:
    def partition(self, s: str) -> List[List[str]]:        
        def isPalindrome(s):
            return s == s[::-1]
        
        res = []
        n = len(s)

        def backtrack(start, arr):
            nonlocal res
            if start == n:
                res.append(arr)
                return
            
            for end in range(start, n):
                if isPalindrome(s[start:end + 1]):
                    backtrack(end + 1, arr + [s[start:end + 1]])
        
        backtrack(0, [])
        return res
            
