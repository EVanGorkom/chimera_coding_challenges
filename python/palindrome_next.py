# A palindrome is any number, word, or phrase that reads the same forward as it does backward. 
# In this challenge, we are going to focus on palindromic numbers. 
# For example, 12321 is a palindromic number, whereas 123 is not.

# Your goal is to write a method/function that takes in an integer and returns the next palindrome. 
# It is safe to assume you are working with only whole numbers, no decimals, and no negatives.

# Example
# find_next_palindrome(100)
# => 101

# find_next_palindrome(101)
# => 111


def find_next_palindrome(num):
  num_str = list(f'{num}')
  array = [int(digit) for digit in num_str]
  
  return array

print(find_next_palindrome(10))