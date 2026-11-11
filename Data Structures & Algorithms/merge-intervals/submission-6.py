class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        res = []
        intervals.sort()

        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]

            while i < len(intervals) and intervals[i][0] <= end:
                end = max(end, intervals[i][1])
                i += 1

            res.append([start, end])

        return res