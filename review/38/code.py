# https://leetcode.com/problems/count-and-say/description/

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = "1"
        for i in xrange(n-1):
            last = ans[0]
            c = 1
            tmp = ""
            for j in xrange(1, len(ans)):
                if ans[j] != last:
                    tmp += "{}{}".format(c, last)
                    last = ans[j]
                    c = 1
                else:
                    c += 1
            tmp += "{}{}".format(c, last)
            ans = tmp
        return ans
        
