"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000

Constraints:
n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
"""

# Initial Thoughts:
# This challenge is pretty similar to ones I've done in the past, but the trick will be to create a sliding window that I will be able to check the values for as I move through the array by the k amount.
# I'll need to be careful not to go over the array length with the window as well and create an "avg" value that dynamically updates while moving though the array.


def findMaxAverage(nums: list[int], k: int) -> float:
    window_sum = sum(nums[0:k])
    max_avg = 0

    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k]
        window_sum = window_sum + nums[i]

        if window_sum > max_sum:
            max_sum = window_sum
    
    return max_avg / k

nums = [1,12,-5,-6,50,3] 
k = 4
print(findMaxAverage(nums, k))
# Answer should be: 12.75000

nums = [5] 
k = 1
print(findMaxAverage(nums, k))
# Answer should be: 5.00000


# WHAT I LEARNED:

