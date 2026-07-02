class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            
            if n in seen:
                break
            seen.add(n)
            temp = 0
            for c in str(n):
                temp += int(c) ** 2
            n = temp
            
        return n == 1