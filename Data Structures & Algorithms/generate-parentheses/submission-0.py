class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curr, opened, closed, opens, closes):
            nonlocal res
            if opens == 0 and closes == 0:
                res.append(curr)
                return
            if opened > closed:
                backtrack(curr + ")", opened, closed + 1, opens, closes - 1)
            if opens > 0:
                backtrack(curr + "(", opened + 1, closed, opens - 1, closes)
        backtrack("", 0, 0, n, n)
        return res
                
                