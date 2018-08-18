# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

from collections import defaultdict

class Solution(object):
    def getCharDist(self, s):
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        return d

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p): return []
        ans = []
        dp = self.getCharDist(p)
        ds_sub = self.getCharDist(s[:len(p)])
        if ds_sub == dp: ans.append(0)
        for i in xrange(1, len(s)-len(p)+1):
            if s[i-1] != s[i+len(p)-1]:
                if ds_sub[s[i-1]] == 1:
                    ds_sub.pop(s[i-1])
                else:
                    ds_sub[s[i-1]] -= 1
                ds_sub[s[i+len(p)-1]] += 1
            if ds_sub == dp: ans.append(i)
        return ans
        
