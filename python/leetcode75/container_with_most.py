"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

# Initial Thoughts:
# I need to move through the array finding the greatest value among the elements both at the beginning and the end. 
# Additionally I'll want to compare the distance between these beginning and end values to see if the distance between them is sizable enough to make the largest area possible.
import pdb

def maxArea(height: list[int]) -> int:
    greatest_area = 0
    left = 0
    right = len(height) - 1
    
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        
        if area > greatest_area:
            greatest_area = area
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return greatest_area


height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
# Answer should be: 49

height = [1,1]
print(maxArea(height))
# Answer should be: 1


# WHAT I LEARNED:
# This one was pretty tricky, but I ended up getting the hang of it.
# It was a really good example of the two-pointer method and I was able to use some creative thinking to arrive at a functional answer.
# I like that the logic I wrote is easy to comprehend and straightforward.
