class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        n = len(s)

        if n == 1:
            return 1
        if n == 2:
            # 0 decodings if 01, 02, 
            if s[0] == "0":
                return 0
            
            # 1 decoding if 10, 20 and 0 decoding if 30, 40, ..
            elif s[1] == "0":
                return 1 if s[0] in "12" else 0

            # 2 decoding if 11, 12, 13, ... 19, 21, 22, ..., 26
            elif 11 <= int(s) <= 26:
                return 2
            
            # 1 decoding if 27, 28, 29, 31, 32, 33, ... 99
            else:
                return 1

        # ways to decode substring up till character number n
        dp = [-1 for _ in range(n)]
        dp[0] = 1 # guaranteed by line 3
        dp[1] = self.numDecodings(s[0:2])

        def help(n):
            if dp[n] == -1:
                if s[n] == "0":
                    if s[n - 1] not in "12":
                        dp[n] = 0
                    else:
                        dp[n] = help(n - 2)
                elif s[n - 1] == "0":
                    dp[n] = help(n - 1)
                elif 10 <= int(s[n - 1:n + 1]) <= 26:
                    dp[n] = help(n - 1) + help(n - 2)
                else:
                    dp[n] = help(n - 1)
            return dp[n]
        
        
        res = help(n - 1)
        print(dp)
        return res



# if 1-9,
    # check number before. if within 1-26, 2 ways
    # e.g. ...48, 1 way. ...12, two ways

# if 0,
    # 1 way: x0.