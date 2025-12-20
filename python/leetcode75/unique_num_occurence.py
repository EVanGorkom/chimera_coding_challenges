"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
"""

# Initial Thoughts
# This is going to be a frequency tracker type of hash problem, which means I'm going to want to use a hash dictionary



def uniqueOccurrences(arr: list[int]) -> bool:
    freq = {}

    for num in arr:
        if num in freq:
            freq[num] = freq[num] + 1
        else:
            freq[num] = 1
        # This means, if 'num' exists, add 1, otherwise add it then it's starting value is 1

    occurrences = freq.values()

    return len(occurrences) == len(set(occurrences))
    # By converting the occurrences to a 'set' it washes the data and removes the duplicates.
    # This then lets us compare the length of the each array of frequencies to see if they do in fact have the same values.



arr = [1,2,2,1,1,3]
print(uniqueOccurrences(arr))
# Answer should be: True

arr = [1,2]
print(uniqueOccurrences(arr))
# Answer should be: False

arr = [-3,0,1,-3,1,1,1,-3,10,0]
print(uniqueOccurrences(arr))
# Answer should be: True


# WHAT I LEARNED:
# I learned that the 'set' function washing the duplicate values out of a collection of data which is interesting and important to know moving forward, especially when it comes to hash problems.
