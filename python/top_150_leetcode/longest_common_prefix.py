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
# I'll want to approach this similar to how I did the majority element challenge. (starting with a base value and then comparing it across the rest of the array)

def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""

    longest_prefix = strs[0]

    for word in strs[1:]:
        while not word.startswith(longest_prefix):
            longest_prefix = longest_prefix[:-1]
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
# I was stumped on how to approach this one for a while after getting into it. As with all of these top 150 challenges, they appear straightforward at first, but are always more challenging than they let on.
# I originally did not want to use the 'while' loop cause I was afraid of compromising my big O time complexity, but ended up deciding that I needed it to progress.
