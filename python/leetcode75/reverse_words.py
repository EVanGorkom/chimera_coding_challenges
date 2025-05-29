"""
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Constraints:
1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
"""

# Initial Thoughts



def reverseWords(s: str) -> str:
    array = s.strip().split()
    return " ".join(reversed(array))



s = "the sky is blue"
print(reverseWords(s))
# Answer should be "blue is sky the"

s = "  hello world  "
print(reverseWords(s))
# Answer should be "world hello"

s = "a good   example"
print(reverseWords(s))
# Answer should be "example good a"


# --------------------------
# WHAT I LEARNED:
# For this challenge I was at first, trying to solve the problem without the use of built-in functions. First I utilized .split(), and then .strip(), and then reversed(). 
# Later I remembered that I could utilize the .join(" ") syntax to join elements of an array together. Afterwards, it was just a matter of stringing all of the builtin methods together in a way that makes sense.
