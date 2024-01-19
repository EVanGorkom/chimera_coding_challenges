# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

# Notes:
# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False
import pdb

def scramble(string, word):
  truth_count = 0
  for letter in (word.lower()):
    if letter in string:
      truth_count += 1

  if truth_count == len(word):
    return True
  else:
    return False
    
print(scramble('rkqodlw', 'world')) #True
print(scramble("katas", "stepakp")) #False
print(scramble('cedewaraaossoqqyt', 'codewars')) #True

print(scramble("abcdefgijkmnpqrstuvwxyz", "Hello")) #False
# print(scramble("abcdefghijklmnopqrstuvwxyz", "Hello"))