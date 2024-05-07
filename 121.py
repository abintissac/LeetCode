class Solution:
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit


# Example usage
solution = Solution()

# Example 1
prices1 = [7, 1, 5, 3, 6, 4]
print("Example 1 Output:", solution.maxProfit(prices1))  # Output: 5

# Example 2
prices2 = [7, 6, 4, 3, 1]
print("Example 2 Output:", solution.maxProfit(prices2))  # Output: 0
