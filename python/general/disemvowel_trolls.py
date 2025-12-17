# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.

# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

# Note: for this kata 'y' isn't considered a vowel.
import pdb

# I want to iterate through the string and find all instances of a,e,i,o, and u and delete/replace them.
def disemvowel(string_):
  vowels = ['a', 'e', 'i', 'o', 'u']
  final_string = string_
  
  for vowel in vowels:
    if vowel or vowel.upper() in final_string:
      final_string = final_string.replace(vowel, '')
      final_string = final_string.replace(vowel.upper(), '')

  return final_string

# # Alternative Solution
# def disemvowel(s):
#     for i in "aeiouAEIOU":
#         s = s.replace(i,'')
#     return s


print(disemvowel("This is a mean sentence with a lot of vowels!!!"))
print(disemvowel("THIS IS A MEAN SENTENCE IN ALL CAPS!!!"))