# https://leetcode.com/problems/number-of-1-bits/description/

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in xrange(32):
            ans += n >> i & 1
        return ans
        
