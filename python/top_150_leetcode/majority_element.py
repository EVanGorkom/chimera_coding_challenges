"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""


# INITIAL SOLUTION:
# def majorityElement(nums: list[int]) -> int:
#     hash = {}
#     majority_count = 0

#     for n in nums:
#         if n in hash:
#             hash[n] += 1
#             if hash[n] > majority_count:
#                 majority_count = hash[n]
#                 majority_element = n
#         else:
#             hash[n] = 1

#     return majority_element


# BOYER-MOORE ALGORITHM
def majorityElement(nums: list[int]) -> int:
    majority_element = None
    count = 0

    for num in nums:
        if count == 0:
            majority_element = num
        count += 1 if num == majority_element else -1

    return majority_element


nums = [3,2,3]
print(majorityElement(nums))
# Answer should be: 3

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))
# Answer should be: 2



# --------------------------
# WHAT I LEARNED:

# The Boyer-Moore Algorithm works well for finding a majority element when we are guaranteed a majority element. 
# My initial solution works well to find a majority element when we are NOT guaranteed a majority element, but the Boyer-Moore Algorithm works best to find the majority element when there is a guaranteed majority and we want to save on space complexity as the challenge requests.