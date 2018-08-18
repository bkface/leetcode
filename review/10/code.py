# https://leetcode.com/problems/regular-expression-matching/description/

import re

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return re.match('^{}$'.format(p), s) is not None
        
