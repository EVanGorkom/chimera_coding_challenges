"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
"""

# Initial Thoughts:
# This is going to be a classic example of sliding windows with a fixed sum. The windows will only ever be k units large and we need to iterate through the string to find the maximum combination of adjacent vowels within that window.


def maxVowels(s: str, k: int) -> int:
    vowels = set("aeiou")
    window_sum = 0
    max_vowels = 0
    left = 0

    for right in range(len(s)):
    # Adds a character from the range to the window
        if s[right] in vowels:
        # Checks if the letter is a vowel
            window_sum += 1
            # if yes, add to the working total

        if right - left + 1 > k:
        # Checks to see if the window is greater than the value of 'k'
            if s[left] in vowels:
            # If yes, and the left-most letter is a vowel...
                window_sum -= 1
                # We need to remove it from the working total
            left += 1
            # Now we need to shrink the left side and keep the window equal to the value of 'k'

        if right - left + 1 == k:
        # Now we check if our window is the same size as 'k'
            max_vowels = max(max_vowels, window_sum)
            # If yes, we want to find the maximum count of vowels and reassign 'max_vowels' to be the higher of either the original max or our working total.

    return max_vowels


s = "abciiidef"
k = 3
print(maxVowels(s, k))
# The answer should be: 3

s = "aeiou"
k = 2
print(maxVowels(s, k))
# The answer should be: 2

s = "leetcode" 
k = 3
print(maxVowels(s, k))
# The answer should be: 2

# WHAT I LEARNED
# I don't think I've studied a lot of fixed sliding window problems before this so this was a nice challenge. It took a second to adapt, but I ended up getting it. Weirdly enough I find it just slightly harder than the variable window problems. I'm definitely gonna practice them more moving forward.
