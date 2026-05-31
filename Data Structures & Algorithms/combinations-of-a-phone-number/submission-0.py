class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        res = []
        n = len(digits)

        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i, sofar):
            if i == n:
                res.append(sofar)
                return
            
            for char in letters[digits[i]]:
                backtrack(i + 1, sofar + char)
        
        backtrack(0, "")
        return res