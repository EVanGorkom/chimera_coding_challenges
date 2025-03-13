"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

import pdb

# Initial Thoughts:
# I'll need to see the entire array to know which day to 'buy' on, and then save it's index. Now only iterate through values moving forward from the buy index forward.
# I'll need to do a comparison operator to determine if the value of the 'buy' value is less than the 'sell' values. Store the difference if there is one.
# Maybe a minimum value function to find the buy value/index and then take a range of the array from that index forward and find the maximum value. Then do a comparison operator. 


def maxProfit(prices: list[int]) -> int:

    ## INITIAL SOLUTION:
    # buy_value = min(prices)
    # potential_sell_prices = prices[(prices.index(buy_value) + 1):]
    # sell_value = 0
    
    # for price in potential_sell_prices:
    #     if price > buy_value and price > sell_value:
    #         sell_value = price

    # if sell_value == 0:
    #     return sell_value
    # else:
    #     return sell_value - buy_value


    ## REFINED SOLUTION:
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

    return max_profit


prices1 = [7,1,5,3,6,4]
print(maxProfit(prices1))
# Answer should be 5

prices2 = [7,6,4,3,1]
print(maxProfit(prices2))
# Answer should be 0



# --------------------------
# WHAT I LEARNED:
# My initial instincts were on the right track, but my first solution iterated through the array too many times for a good big O solution. 
# I knew there was a better way to solve the problem without iterating and recreating the array each time.
# I referenced my other two-pointer iteration solution problems and was able to come up with an answer that made sense for this use case and saved on both time and memory complexity.

