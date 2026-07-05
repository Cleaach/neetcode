class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lasts = {}
        for i, c in enumerate(s):
            lasts[c] = i

        n = len(s)
        res = []
        
        p = 0
        while p < n:
            end = lasts[s[p]]
            size = 0

            while p <= end:
                end = max(end, lasts[s[p]])
                p += 1
                size += 1
            
            res.append(size)
        
        return res

