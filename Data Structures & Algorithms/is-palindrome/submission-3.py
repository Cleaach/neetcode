class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = []
        for char in s:
            if char.lower() in "abcdefghijklmnopqrstuvwxyz0123456789":
                alpha.append(char.lower())
        return alpha == alpha[::-1]