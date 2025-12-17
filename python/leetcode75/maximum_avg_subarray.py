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
# For this challenge I'm definitely going to need to use the static window version of a Sliding window. I think the challenge here is going to be handling the trailing zeros. I'm not sure why they are being included here.


def findMaxAverage(nums: list[int], k: int) -> float:
    window_sum = 0
    max_avg = float("-inf")
    left = 0

    for right in range(len(nums)):
        window_sum += nums[right]
        
        if right - left + 1 == k:
            window_avg = window_sum / k
            max_avg = max(max_avg, window_avg)
            window_sum -= nums[left]
            left += 1

    return max_avg



nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums, k))
# Answer should be: 12.75000


nums = [5]
k = 1
print(findMaxAverage(nums, k))
# Answer should be: 5.00000

# WHAT I LEARNED:
# After taking some time away from coding challenges, it was nice to get back into the swing of things with this one.
# I think this one was pretty straight forward after reviewing my notes and I enjoyed solving it. 
# Looking around the internet I found that I'm calculating the average on the inside of the loop, but since 'k' is a fixed number, it's unnecessary to do so
# within the loop and I can instead just solve for the max sum and calculate average at the end! Neat trick!
