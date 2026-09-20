class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp =0

        l,r = 0, 1

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                mp = max(profit, mp)
            
            else:
                l = r
            
            r += 1
        
        return mp