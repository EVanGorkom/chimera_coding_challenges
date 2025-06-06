"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:
0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""

# Initial Thoughts:
# Off the bat, this one is going to be tricky. The trick here will be that I need to comb through both the strings but limit the for loop to only one pass.
# The initial solution works, but it needs to be refined and fails on certain edge cases.


def isSubsequence(s: str, t: str) -> bool:
    s_point = 0
    t_point = 0

    while s_point < len(s) and t_point < len(t):
        if s[s_point] == t[t_point]:
            s_point += 1
        t_point += 1
    
    return s_point == len(s)


s = "abc" 
t = "ahbgdc"
print(isSubsequence(s, t))
# Answer should be: true

s = "axc"
t = "ahbgdc"
print(isSubsequence(s, t))
# Answer should be: false


# WHAT I LEARNED:
# I feel like this was a really good challenge to learn the classic basics of two-pointer method and I feel like my first method, while accurate could have used some improvements.
# I ended switching to a 'while' loop instead of a for loop since I wasn't really using the 'i' variable anyways. I also streamlined the final return into single comparison operator since it was returning True or False anyways.
# All in all a good challenge and I feel like I learned a lot.
