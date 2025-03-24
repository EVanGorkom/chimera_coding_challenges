"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""

# Initial thoughts
# I feel like this one is fairly straightforward. I'll want to compare the full value of the 'needle' with the haystack and see if it is in there at all.
# I think the trick here is going to be keeping track of the index value in which a match first occurs.
# However, as I work through this, I'm going to not only need to find the match, but I will need to find out if the whole word matches, and if yes, where that word starts.


def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    needle_length = len(needle)
    haystack_length = len(haystack)

    for i in range(haystack_length - needle_length + 1):
        if haystack[i:i + needle_length] == needle:
            return i

    return -1



haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))
# Answer should be 0

haystack = "leetcode"
needle = "leeto"
print(strStr(haystack, needle))
# Answer should be -1


# --------------------------
# WHAT I LEARNED:
# This one, of course, was NOT easy. It took me a long time to figure out the HOW of how to find the starting index of the haystack where the needle was.
# To be completely honest, I had to get help from Chat to get the idea for the 'walking' range. I knew that I would need to iterate through the range step by step and compare the substring by the length of my needle's string, but I was getting stumped on how to create that range to begin with.
