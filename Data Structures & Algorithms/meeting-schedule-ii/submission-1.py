"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count = 0
        res = 0
        arr = [] # (time, start | end)
        for i in intervals:
            arr.append((i.start, 'start'))
            arr.append((i.end, 'end'))
        def tie(s):
            return 0.5 if s == 'start' else 0
        arr.sort(key=lambda x: x[0] + tie(x[1]))

        for t, e in arr:
            if e == 'start':
                count += 1
            if e == 'end':
                count -= 1
            res = max(res, count)
        
        return res