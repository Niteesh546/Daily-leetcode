class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        i=0
        while i< len(intervals)-1:
            current_end = intervals[i][1]
            next_start = intervals[i+1][0]

            if next_start <= current_end:
                intervals[i][0] = min(intervals[i][0], intervals[i+1][0])
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])

                intervals.pop(i+1)
    
            else:
               i+=1
        return intervals

        
        