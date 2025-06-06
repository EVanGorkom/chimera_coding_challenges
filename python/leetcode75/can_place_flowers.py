"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:
1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""

# Initial Thoughts
# I'll need to likely utilize a two-pointer method to find out the previous values with the current or next values



def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    flowerbed_size = len(flowerbed)
    for i in range(flowerbed_size):
        if n <= 0:
            break
        prev = i == 0 or flowerbed[i - 1] == 0
        fut = i == flowerbed_size - 1 or flowerbed[i + 1] == 0
        if prev and fut and flowerbed[i] == 0:
            flowerbed[i] = 1
            n -= 1
    return n <= 0


flowerbed = [1,0,0,0,1] 
n = 1
print(canPlaceFlowers(flowerbed, n))
# Answer should be: true

flowerbed = [1,0,0,0,1] 
n = 2
print(canPlaceFlowers(flowerbed, n))
# Answer should be: false


# --------------------------
# WHAT I LEARNED:
# I learned that I need to study basic/advanced algorithmic patterns more. 