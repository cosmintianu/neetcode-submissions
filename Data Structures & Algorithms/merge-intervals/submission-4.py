class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        
        intervals.sort()

        left_min = intervals[0][0]
        right_max = intervals[0][1]

        
        for i, (start, end) in enumerate(intervals):
            
            if end > right_max:
                right_max = end

            

            if i == len(intervals) - 1:
                res.append([left_min, right_max])

            if i + 1 < len(intervals) and right_max < intervals[i + 1][0]:
                res.append([left_min, right_max])
                left_min = intervals[i+1][0]
                right_max = intervals[i+1][1]

        return res