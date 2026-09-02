class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        maxDiff = 0
        cheapestPrice = 101

        while i < len(prices):
            cheapestPrice = min(cheapestPrice, prices[i])
            difference = prices[i] - cheapestPrice
            maxDiff = max(maxDiff, difference)
            i += 1
        
        return maxDiff