# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
        # profitmax = 0
        # l = 0
        # for r in range(len(prices)) :
        #     if prices[l] >= prices[r] : #loss days or 0 profit days
        #         l = r #bcz if cp > sp, make cp as sp, as sp is lower 
        #     else : #profit day
        #         profit = prices[r] - prices[l]
        #         profitmax = max(profitmax,profit)
        # return profitmax



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profitmax = 0
        l = 0
        for r in range(len(prices)) :
            profit = prices[r] - prices[l]
            
            if profit > 0 :
                profitmax = max(profitmax, profit)
                
            else:
                l = r
        return profitmax





















