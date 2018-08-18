# https://leetcode.com/problems/multiply-strings/description/

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = 0
        for j in xrange(len(num2)-1, -1, -1):
            for k in xrange(len(num1)-1, -1, -1):
                order = len(num1)- k - 1 + len(num2) - j - 1
                ans += int(num2[j]) * int(num1[k]) * (10**order)
        return str(ans)
#          23
#         456
#     --------
#         138
#        115
#        92
#     --------
#       10488
