class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for i in prices:
            if i < buy:
                buy = i
            elif i - buy > profit:
                profit = i - buy
        return profit