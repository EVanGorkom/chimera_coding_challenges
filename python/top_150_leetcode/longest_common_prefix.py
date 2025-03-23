"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog", "racecar", "car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

# Initial thoughts:
# I'll want to approach this similar to how I did the majority element challenge. (starting with a base value and )

def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""

    # Start with the first word as the initial prefix
    longest_prefix = strs[0]

    # Iterate over the remaining words
    for word in strs[1:]:
        # While the current word does not start with the current prefix,
        # remove the last character from the prefix
        while not word.startswith(longest_prefix):
            longest_prefix = longest_prefix[:-1]
            # If the prefix becomes empty, no common prefix exists
            if not longest_prefix:
                return ""

    return longest_prefix


strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))
# Answer should be "fl"

strs = ["dog", "racecar", "car"]
print(longestCommonPrefix(strs))
# Answer should be ""


# --------------------------
# WHAT I LEARNED: