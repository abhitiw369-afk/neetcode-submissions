class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profitmax = 0
        l = 0
        for r in range(len(prices)) :
            if prices[l] >= prices[r] : #loss days or 0 profit days
                l = r
            else : #profit day
                profit = prices[r] - prices[l]
                profitmax = max(profitmax,profit)
        return profitmax