"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.
"""

# Initial Thoughts:



def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    set1 = set(nums1)
    set2 = set(nums2)

    return [
        list(set1 - set2),
        list(set2 - set1)
    ]



nums1 = [1,2,3] 
nums2 = [2,4,6]
print(findDifference(nums1, nums2))
# Answer should be: [[1,3],[4,6]]

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
print(findDifference(nums1, nums2))
# Answer should be: [[3],[]]


# WHAT I LEARNED:
# This is stupid that it works like that. My initial build-out implemented a lot of for loops and such to iterate through things to find the missing values.
# I ended up refactoring a few times before looking up some tips and found that I could literally just make them 'sets' and subtract them from each other.

