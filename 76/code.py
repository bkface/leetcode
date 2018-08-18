# https://leetcode.com/problems/minimum-window-substring/description/

from collections import defaultdict

class Solution(object):
    def equal(self, dt, dw):
        for key in dt.keys():
            if key not in dw or dt[key] > dw[key]:
                return False
        return True
    
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""
        
        ds = defaultdict(int)
        for c in s:
            ds[c] += 1

        dt = defaultdict(int)
        for c in t:
            if c not in ds:
                return ""
            dt[c] += 1

        for key in dt.keys():
            if dt[key] > ds[key]:
                return ""

        S = [i for i in zip(range(len(s)), s) if i[1] in dt]

        ws = len(t)
        while ws <= len(S):
            min_ = None
            for i in xrange(len(S)-ws+1):
                ws_ = S[i+ws-1][0] - S[i][0]
                if min_ is None or ws_ < min_[0]:
                    min_ = (ws, i, i+ws-1)

            dw = defaultdict(int)
            for k in xrange(min_[1], min_[2]+1):
                dw[S[k][1]] += 1
            if self.equal(dt, dw):
                return s[S[i][0]:S[i+ws-1][0]+1]
            ws += 1
        return ""
        
