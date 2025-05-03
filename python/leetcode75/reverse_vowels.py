"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"

Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:
1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""

# Initial Thoughts
# I wonder if there's a way to iterate through a string backwards? I think it would be beneficial to move through the string both backwards and forwards, and assign and reassign values as we move through either end.
# For this strategy I would need to know the midpoint of the string. If it's a vowel, I leave it alone, else continue switching the vowels.
# Additionally, I'll need to define the vowels array of strings before hand. I'll need to account for uppercase or lowercase characters.


def reverseVowels(s: str) -> str:
    return


s = "IceCreAm"
print(reverseVowels(s))
# Answer should be: AceCreIm

s = "leetcode"
print(reverseVowels(s))
# Answer should be: leotcede


# --------------------------
# WHAT I LEARNED:
