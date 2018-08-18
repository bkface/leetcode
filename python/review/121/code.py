# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        maxP = 0
        maxV = prices[-1]
        for i in xrange(len(prices)-2, -1, -1):
            if prices[i] > maxV:
                maxV = prices[i]
                continue
            profit = maxV-prices[i]
            if maxP < profit:
                maxP = profit
        return maxP
        
