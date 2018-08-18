# https://leetcode.com/problems/group-anagrams/description/

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(list)
        for s in strs:
            d[''.join(sorted(s))].append(s)
        return d.values()
        
