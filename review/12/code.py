# https://leetcode.com/problems/integer-to-roman/description/

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romans = [(1000, 'M'), \
                  (900, 'CM'), \
                  (500, 'D'), \
                  (400, 'CD'), \
                  (100, 'C'), \
                  (90, 'XC'), \
                  (50, 'L'), \
                  (40, 'XL'), \
                  (10, 'X'), \
                  (9, 'IX'), \
                  (5, 'V'), \
                  (4, 'IV'), \
                  (1, 'I')]

        pt = 0
        ans = ""
        while(pt < len(romans)):
            c = num/romans[pt][0]
            for i in xrange(c):
                ans += romans[pt][1]
            if c > 0:
                num -= c * romans[pt][0]
            pt += 1
        return ans
        
