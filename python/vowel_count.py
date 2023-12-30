# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

## Initial solution (no refactor) 
# def get_count(sentence):
#   count = 0
#   count += sentence.count("a")
#   count += sentence.count("e")
#   count += sentence.count("i")
#   count += sentence.count("o")
#   count += sentence.count("u")
#   return count

## Refactored solution
def get_count(sentence):
  vowels = "aeiouAEIOU"
  count = sum(sentence.count(vowel) for vowel in vowels)
  return count

  # here we're looking at each char in the sentence.
  #   is char == vowel from vowels string?
  #     add to the count if it is!

print(get_count("This is a long sentence with a lot of vowels for counting."))