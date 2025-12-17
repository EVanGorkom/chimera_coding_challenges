import pytest
import pdb

# Write a function that counts how many different ways you can make change for an amount of money, given an array of coin denominations. For example, there are 3 ways to give change for 4 if you have coins with denomination 1 and 2:

# 1+1+1+1, 1+1+2, 2+2.
# The order of coins does not matter:

# 1+1+2 == 2+1+1
# Also, assume that you have an infinite amount of coins.

# Your function should take an amount to change and an array of unique denominations for the coins:

#   count_change(4, [1,2]) # => 3
#   count_change(10, [5,2,3]) # => 4
#   count_change(11, [5,7]) # => 0

## Using recursion (works until stack overflow error)
# def count_change(money, coins):      
#     def count_combinations(amount, index):
#         if amount == 0:
#             return 1
        
#         if amount < 0 or index >= len(coins):
#             return 0
        
#         include_current = count_combinations(amount - coins[index], index)
#         exclude_current = count_combinations(amount, index + 1)
        
#         return include_current + exclude_current
#     return count_combinations(money, 0)

## Using iteration
def count_change(money, coins):
    dp = [0] * (money + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, money + 1):
            # pdb.set_trace()
            dp[i] += dp[i - coin]

    return dp[money]


# Basic test case
print(count_change(4, [1,2])) # => 3
print(count_change(10, [5,2,3])) # => 4
print(count_change(11, [5,7])) # => 0

# Pytest test case
def test_count_change():
    assert count_change(4, [1, 2]) == 3
    assert count_change(10, [5, 2, 3]) == 4
    assert count_change(11, [5, 7]) == 0
    assert count_change(0, [1, 2]) == 1