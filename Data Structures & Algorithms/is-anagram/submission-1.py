class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        for char in s:
            if (char not in d):
                d[char] = 1
            else:
                d[char] += 1
        for char in t:
            if (char not in d or d[char] == 0):
                return False
            else:
                d[char] -= 1
        for i in d.values():
            if (i != 0) :
                return False
        return True