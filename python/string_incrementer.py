# Your job is to write a function which increments a string, to create a new string.

# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.

# Examples:
# foo -> foo1
# foobar23 -> foobar24
# foo0042 -> foo0043
# foo9 -> foo10
# foo099 -> foo100

# Attention: If the number has leading zeros the amount of digits should be considered.

import pdb

# def increment_string(input):
#   if len(input) == 0:
#     return "1"

#   last_char = input[-1]

#   if last_char.isdigit():
#     incremented_digit = str(int(last_char) + 1)
#     input = input[:-1] + incremented_digit
#   else:
#     input += '1'

#   return input


def increment_string(s):
  prefix = s.rstrip('0123456789')
  suffix = s[len(prefix):]

  if suffix == '':
    return s + '1'
  else:
    incremented_number = str(int(suffix) + 1).zfill(len(suffix))
    return prefix + incremented_number

print(increment_string("Hello World1"))
print(increment_string("Stay positive!"))
print(increment_string(""))
