class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        min_val = prices[0]
        for i in range(len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]

            max_profit = max(max_profit, prices[i] - min_val)

        return max_profit