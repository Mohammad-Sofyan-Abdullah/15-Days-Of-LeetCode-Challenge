class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
#         min_price = min(prices)
#         print(min_price)
        
#         index = prices.index(min_price)
#         print(index)
        
#         profits = []
        
#         for i in range(index + 1, len(prices)):
#             diff = prices[i] - min_price
#             profits.append(diff)
        
#         print(profits)
        
#         max_profit = 0
        
#         if len(profits) == 0:
#             max_profit = 0
#         else:
#             max_profit = max(profits)
        
#         return max_profit


        if not prices or len(prices) == 1:
            return 0
        
        min_price = float('inf')
        max_profit = 0 
        
        for price in prices:
            if price < min_price:
                min_price = price
            
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        
        return max_profit
            