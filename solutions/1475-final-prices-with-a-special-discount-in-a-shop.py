"""
Given the array prices where prices[i] is the price of the ith item in a shop. There is a special discount for items in the shop, if you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i], otherwise, you will not receive any discount at all.

Return an array where the ith element is the final price you will pay for the ith item of the shop considering the special discount.

"""
from typing import List
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        Greedy, not optimal O(n^2)
        """
        # n = len(prices)
        # new_prices = []
        # for i in range(n):
        #     new_prices.append(prices[i])
        #     for j in range(i+1, n):
        #         if prices[j] <= prices[i]:
        #             new_prices.pop()
        #             new_prices.append(prices[i] - prices[j])
        #             break
        # return new_prices

        # New, after studying the discussions: O(n)
        sol, stack = prices, []
        for i, price in enumerate(prices):
            while stack and (sol[stack[-1]] >= price):
                sol[stack.pop()] -= price
            stack.append(i)
        return sol
