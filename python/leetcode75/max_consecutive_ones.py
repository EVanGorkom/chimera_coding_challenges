"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's. 

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6

Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10

Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""


# Initial Thoughts:
# This problem has weird wording, but effectivelyI want to find out what the longest possible subarray of 1s can be if I were to replace 'k' amount of 0s with 1s.
# This will be a little tricky, but I think the basic concept will be a relatively straight forward sliding window strategy.


def longestOnes(nums: list[int], k: int) -> int:
    return


nums = [1,1,1,0,0,0,1,1,1,1,0] 
k = 2
print(longestOnes(nums, k))
# The answer should be 6

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(longestOnes(nums, k))
# The answer should be 10


# WHAT I LEARNED


