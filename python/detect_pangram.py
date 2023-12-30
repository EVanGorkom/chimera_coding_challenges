# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

def is_pangram(sentence):
  letters = "abcdefghijklmnopqrstuvwxyz"
  return all(letter in sentence.lower() for letter in letters)

## Original Solution:
# def is_pangram(sentence):
  # for letter in letters:
  #   if (letter in sentence.lower()):
  #     return True
  #   else:
  #     return False


print(is_pangram("The quick, brown fox jumps over the lazy dog!")) #True
print(is_pangram("1bcdefghijklmnopqrstuvwxyz")) #False
print(is_pangram("abcdefghijklmnopqrstuvwxyz")) #True
print(is_pangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ")) #True