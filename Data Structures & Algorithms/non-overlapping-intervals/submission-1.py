class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda pair : pair[0])

        result = [intervals[0]]
        cnt = 0
        for start, end in intervals[1:]:
            lastEnd = result[-1][1]

            if start < lastEnd:
                cnt += 1
                result.append([start, min(end, lastEnd)])
            else:
                result.append([start, end])

        return cnt