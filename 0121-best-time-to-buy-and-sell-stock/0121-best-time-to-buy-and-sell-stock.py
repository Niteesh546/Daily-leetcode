class Solution(object):
    def maxProfit(self, prices):
        min_p = prices[0]
        max_pro = 0

        for i in range(1,len(prices)):
            if prices[i]<min_p:
                min_p = prices[i]
            else:
                profit = prices[i]-min_p
                if profit > max_pro:
                    max_pro = profit
        return max_pro

        
        