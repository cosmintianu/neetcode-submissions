class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        left, right = 0, 0
        res = []
        intervals.sort()

        while right < len(intervals):
            start = intervals[right][0]
            end = intervals[right][1]

            while right < len(intervals) and intervals[right][0] <= end:
                end = max(end, intervals[right][1])
                right += 1

            res.append([start, end])

        return res