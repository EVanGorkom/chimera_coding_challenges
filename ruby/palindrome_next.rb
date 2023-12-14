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


# I want the value of num to be less than my final result. 
# I need to be able to count the length of the num, and reflect the first values to the back.
def find_next_palindrome(num)
  string_num = num.to_s
  length = string_num.length
  copy_length = length / 2

  return 11 if length == 1 || num == 10
  
  if length.even?
    first_half = string_num.slice(0, copy_length)
    second_half = string_num.slice(copy_length..-1)
    if first_half.to_i < second_half.to_i
      new_num_half = first_half.to_i + 1
      reverse = new_num_half.to_s.reverse
      final = new_num_half.to_s + reverse
    else 
      final = first_half + first_half.reverse
    end
  else
    mid_point = string_num[(length / 2)]
    string_num.delete(mid_point)
    first_half = string_num.slice(0, copy_length)
    second_half = string_num.slice((length / 2)..-1)
    if first_half.to_i < second_half.to_i
      final = first_half + (mid_point.to_i + 1).to_s + first_half.reverse
    else
      final = first_half + mid_point + first_half.reverse
    end
  end
  final.to_i
end

p find_next_palindrome(12134)
p find_next_palindrome(123)
p find_next_palindrome(9876)
p find_next_palindrome(10023)
p find_next_palindrome(12)
p find_next_palindrome(101)
