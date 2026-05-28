from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # Count required characters
        target = defaultdict(int)
        for char in t:
            target[char] += 1
        
        # Track how many unique characters in t have been satisfied
        required = len(target)  # Number of unique chars we need to satisfy
        formed = 0             # Number of unique chars currently satisfied
        
        # Current window
        window = defaultdict(int)
        
        l = 0
        res = (float("inf"), 0, 0)  # (length, left, right)
        
        for r in range(len(s)):
            char = s[r]
            window[char] += 1
            
            # If frequency of current char matches target, increment formed
            if char in target and window[char] == target[char]:
                formed += 1
            
            # Try to shrink window from left
            while l <= r and formed == required:
                char = s[l]
                
                # Update result if current window is smaller
                if r - l + 1 < res[0]:
                    res = (r - l + 1, l, r)
                
                # Remove character from left
                window[char] -= 1
                if char in target and window[char] < target[char]:
                    formed -= 1
                
                l += 1
        
        # Return the smallest window or empty string
        return "" if res[0] == float("inf") else s[res[1]:res[2] + 1]