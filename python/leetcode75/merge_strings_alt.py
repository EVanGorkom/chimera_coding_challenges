"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d


Constraints:
1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""

# Initial thoughts
# The trick here is going to be "how do I iterate through both strings at the same time?".
# I need to be able to alternate between two strings and add the element from each string for each index one at a time.


def mergeAlternately(word1: str, word2: str) -> str:
    final = ""
    i = 0
    j = 0

    while i < len(word1) or j < len(word2):
        if i < len(word1):
            final += word1[i]
            i += 1
        if j < len(word2):
            final += word2[j]
            j += 1

    return final


word1 = "abc"
word2 = "pqr"
print(mergeAlternately(word1, word2))
# Answer should be "a p b q c r"

word1 = "ab"
word2 = "pqrs"
print(mergeAlternately(word1, word2))
# Answer should be "a p b q r s"

word1 = "abcd"
word2 = "pq"
print(mergeAlternately(word1, word2))
# Answer should be "a p b q c d"


# WHAT I LEARNED:
# I was able to deduce that I would need to track how long the strings were while iterating through each string simultaneously.
# Initially I tried creating only one counting value "i", but after doing a lot of troubleshooting and working around, I ultimately decided that I needed two counting values.
# The problem was fairly straightforward after that and I only needed to do some clean up work to make the code more refined.
