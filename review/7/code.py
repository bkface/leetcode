# https://leetcode.com/problems/reverse-integer/description/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        positive = x >= 0
        x_ = str(x) if positive else str(x)[1:]
        ans = long(''.join(reversed(list(x_))))

        if positive:
            if ans >= 2**31 - 1:
                return 0
            else:
                return ans
        else:
            if ans >= 2**31:
                return 0
            else:
                return -1 * ans
