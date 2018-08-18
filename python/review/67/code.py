# https://leetcode.com/problems/add-binary/description/

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m = max(len(a), len(b))
        carry = 0
        ans = ""
        for i in xrange(m):
            va = int(a[len(a)-i-1]) if i < len(a) else 0
            vb = int(b[len(b)-i-1]) if i < len(b) else 0
            s = va + vb + carry
            ans = "{}{}".format(s%2, ans)
            carry = s/2
        if carry > 0:
            return "{}{}".format(carry, ans)
        return ans
        
