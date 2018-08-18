# https://leetcode.com/problems/meeting-rooms/description/

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if len(intervals) < 1: return True
        intervals.sort(key=lambda x: x.start)
        cur_itv = intervals[0]
        for itv in intervals[1:]:
            if cur_itv.end > itv.start:
                return False
            cur_itv = itv
        return True
        
