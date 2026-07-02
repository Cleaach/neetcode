class MedianFinder:

    def __init__(self):
        self.odd = False
        self.top = []
        heapq.heapify(self.top)
        self.bottom = []
        heapq.heapify_max(self.bottom)
        self.median = 0

    def addNum(self, num: int) -> None:
        self.odd = not self.odd

        # put at top
        if self.bottom and num > self.bottom[0]:
            heapq.heappush(self.top, num)
            
            # handle imbalance
            if len(self.top) > len(self.bottom):
                n = heapq.heappop(self.top)
                heapq.heappush_max(self.bottom, n)
        
        # put at bottom
        else:
            heapq.heappush_max(self.bottom, num)

            # handle imbalance
            if len(self.bottom) - len(self.top) > 1:
                n = heapq.heappop_max(self.bottom)
                heapq.heappush(self.top, n)
        
        self.median = self.bottom[0] if self.odd else (self.bottom[0] + self.top[0]) / 2

    def findMedian(self) -> float:
        return self.median

        