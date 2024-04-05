# class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
def twoSum(nums, target):
    ## Solution 1 (Double iteration)
    # n = len(nums)

    # for i in range(n):
    #     for j in range(i + 1, n):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]
    
    # return []

    # Solution 2 (Hashmap usage)
    num_indices = {}
    # Iterate through the list
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num
        
        # Check if the complement is in the dictionary
        if complement in num_indices:
            # Return the indices of the two numbers that add up to the target
            return [num_indices[complement], i]
        
        # Add the current number and its index to the dictionary
        num_indices[num] = i
    
    # If no solution is found, return an empty list (or raise an exception)
    return []

def test_two_sum():
    assert twoSum([1, 2, 3, 4, 5], 8) == [2, 4]
    assert twoSum([1, 1, 2, 3, 4, 5], 2) == [0, 1]
    assert twoSum([1, 2, 3, 4, 5, 15], 20) == [4, 5]