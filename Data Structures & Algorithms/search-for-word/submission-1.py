class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        found = False

        def search(i, j, remaining):
            nonlocal found

            if remaining == "":
                found = True
                return
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if board[i][j] == "*":
                return
            if board[i][j] == remaining[0]:
                temp = board[i][j]
                board[i][j] = "*"
                search(i + 1, j, remaining[1:])
                search(i - 1, j, remaining[1:])
                search(i, j + 1, remaining[1:])
                search(i, j - 1, remaining[1:])
                board[i][j] = temp
        
        for i in range(m):
            for j in range(n):
                search(i, j, word)
        
        return found

                
