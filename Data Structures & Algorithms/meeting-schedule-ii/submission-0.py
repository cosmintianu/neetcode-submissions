"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []

        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)

        start.sort()
        end.sort()
        res = 0
        s, e = 0, 0
        cnt = 0
        while s < len(intervals) and e < len(intervals):
            while s < len(intervals) and start[s] < end[e]:
                cnt += 1
                s += 1

            res = max(res, cnt)
            e += 1
            cnt -= 1

        return res






