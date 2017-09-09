# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if (len(intervals) == 0):
            return []
        
        # First, sort the list of intervals by each element's start
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        
        ret = [sorted_intervals[0]]    # Push first interval to return list
        
        for i in range(1, len(intervals)):
            curr_interval = sorted_intervals[i]
            
            if (ret[-1].end < curr_interval.start):
                # If the interval has no overlap with last interval,
                # Just push the interval to sint
                ret.append(curr_interval)
                
            else:
                # There is overlap. merge intervals
                ret[-1].end = max(ret[-1].end, curr_interval.end)
                
        return ret
    

