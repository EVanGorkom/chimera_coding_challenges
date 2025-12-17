# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.

def count(input):
  count_dict = {}
  for letter in input:
    count_dict[letter] = count_dict.get(letter, 0) + 1
  return count_dict

print(count("abcd"))
print(count("aabbcc"))
print(count("abbcccdddd"))