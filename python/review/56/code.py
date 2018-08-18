# https://leetcode.com/problems/merge-intervals/description/

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
        if len(intervals) < 1: return []
        intervals.sort(key=lambda x: x.start)
        ans = []
        cur_itv = intervals[0]
        for itv in intervals:
            if cur_itv.end >= itv.start:
                if itv.end > cur_itv.end:
                    cur_itv.end = itv.end
            else:
                ans.append(cur_itv)
                cur_itv = itv
        ans.append(cur_itv)
        return ans
        
