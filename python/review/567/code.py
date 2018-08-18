# https://leetcode.com/problems/permutation-in-string/description/

from collections import defaultdict

class Solution(object):
    def getCharDist(self, s):
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        return d

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2): return False

        ds1 = self.getCharDist(s1)
        ds2_sub = self.getCharDist(s2[:len(s1)])
        if ds1 == ds2_sub: return True

        for i in xrange(1, len(s2)-len(s1)+1):
            if s2[i-1] != s2[i+len(s1)-1]:
                if ds2_sub[s2[i-1]] == 1:
                    ds2_sub.pop(s2[i-1])
                else:
                    ds2_sub[s2[i-1]] -= 1
                ds2_sub[s2[i+len(s1)-1]] += 1
            if ds1 == ds2_sub: return True
        return False
        
