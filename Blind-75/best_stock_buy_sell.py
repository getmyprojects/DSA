"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Ex:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Note: Leetcode 121
"""


class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        l,r = 0,1
        while r<len(prices):
            if prices[l] < prices[r]:
                max_profit = max(prices[r]-prices[l], max_profit)
            else:
                l = r
            r += 1
        return max_profit


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    obj = Solution()
    res = obj.maxProfit(prices)
    print(res)

    prices1 = [7,6,4,3,1]
    res = obj.maxProfit(prices1)
    print(res)