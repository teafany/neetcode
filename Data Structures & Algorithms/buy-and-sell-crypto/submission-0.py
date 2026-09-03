class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, max_profit = 0, 1, 0

        for price in prices:
            while r < len(prices):
                curr_profit = prices[r] - prices[l]
                max_profit = max(max_profit, curr_profit)
                if prices[l] > prices[r]:
                    l = r
                r += 1
            return max_profit