"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

Constraints:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""

import math

# Initial thoughts
# Finding the strings that match, if any, will be the easy part. I think finding the longest string that matches will be the trick here.
# I'll want to first check if the strings match anywhere (example 3), then for how long (example 1), then see if it can be reduced at all (example 2).


def gcdOfStrings(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""
    
    gcd_length = math.gcd(len(str1), len(str2))
    return str1[:gcd_length]


str1 = "ABCABC"
str2 = "ABC"
print(gcdOfStrings(str1, str2))
# Answer should be "ABC"

str1 = "ABABAB"
str2 = "ABAB"
print(gcdOfStrings(str1, str2))
# Answer should be "AB"

str1 = "LEET"
str2 = "CODE"
print(gcdOfStrings(str1, str2))
# Answer should be ""


# --------------------------
# WHAT I LEARNED:
# This one was pretty tricky. I began with iterating through both strings to find commonality, but my solution failed at reducing the redundant characters.
# I had to do some research on this one to learn that the GCD MUST be a repeating pattern of at least one of the strings. For example I was initially under the impression that and example like `str1 = abcdef` and `str2 = abc` would still return the GCD of "abc", but that isn't how the challenge works.
# With this realization I was able to simplify my code and found the `math.gcd()` function which I did not know existed previously. 
# Finally I took the range of the string that was the GCD's length.
