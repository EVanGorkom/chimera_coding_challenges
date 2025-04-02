"""
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies.

Example 1:
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

Example 2:
Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false] 
Explanation: There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.

Example 3:
Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]

Constraints:
n == candies.length
2 <= n <= 100
1 <= candies[i] <= 100
1 <= extraCandies <= 50
"""

# Initial thoughts
# This challenge will require me to check the values of each kid's candy count before and after the extra candies are added.
# I think I'll start with taking the maximum value of the array and then loop through once to see if the extra candies added for each value are greater than or equal to the maximum base value.
#   If yes, then I can add `True` to the solution array, else add `False`

import pdb

def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    greatest_candies = max(candies)
    bool_array = []
    
    for kid in candies:
        if kid + extraCandies >= greatest_candies:
            bool_array.append(True)
        else:
            bool_array.append(False)

    return bool_array


candies = [2,3,5,1,3] 
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))
# Answer should be: [true,true,true,false,true] 

candies = [4,2,1,1,2] 
extraCandies = 1
print(kidsWithCandies(candies, extraCandies))
# Answer should be: [true,false,false,false,false] 

candies = [12,1,12] 
extraCandies = 10
print(kidsWithCandies(candies, extraCandies))
# Answer should be: [true,false,true]


# --------------------------
# WHAT I LEARNED:
# I don't think I really learned anything on this one that was too out of the ordinary. 
# I tackled this step by step and made sure to read the prompt very carefully to fully understand the requirements of the code.
# Then I utilized the built-in methods and compared values.
