"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

# Initial Thoughts:
# I'll need to make sure that I'm only iterating through the array once, but we still need to see all the values of the array at each index of the array.


def productExceptSelf(nums: list[int]) -> list[int]:
    result = []
    
    for num in nums:
        return


nums = [1,2,3,4]
print(productExceptSelf(nums))
# The answer should be: [24,12,8,6]

nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))
# The answer should be: [0,0,9,0,0]


# --------------------------
# WHAT I LEARNED:

