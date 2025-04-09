class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            best_price = min(best_price, prices[i])
            max_profit = max(max_profit, prices[i] - best_price)
        
        return max_profit

        