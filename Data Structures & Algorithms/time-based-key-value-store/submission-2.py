class TimeMap:

    def __init__(self):
        self.h = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.h.keys():
            self.h[key] = []

        self.h[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.h.keys():
            return ""
        
        # binary search to find value with greatest timestamp_prev <= timestamp
        x = self.h[key]
        l = 0
        r = len(x) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2

            if x[m][1] <= timestamp:
                res = x[m][0]
                l = m + 1
            
            if x[m][1] > timestamp:
                r = m - 1
            
        return res