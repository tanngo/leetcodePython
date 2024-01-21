# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1144565404/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit =0
        min_price = float('inf')
        for price in prices:
            print(price)
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit


    # def maxProfit(self, prices: List[int]) -> int:
    #     max_profit =0
    #     for i in range(len(prices)-1):
    #         for j in range(i+1,len(prices)):
    #             max_profit= max(max_profit,prices[j]-prices[i])

    #     return max_profit