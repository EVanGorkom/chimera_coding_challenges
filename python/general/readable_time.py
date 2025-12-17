# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.
import pdb

def make_readable(input):
  if input > 356399:
    final = "99:59:59"
  else:
    hours = 0
    minutes = 0
    seconds = 0

    while input > 59:
      input -= 60
      minutes += 1
      if minutes > 59:
        minutes = 0
        hours += 1
    seconds = input

    final = f"{hours:02}:{minutes:02}:{seconds:02}"
    # if len(str(seconds)) == 1:
    #   seconds = '0' + str(seconds)
    # if len(str(minutes)) == 1:
    #   minutes = '0' + str(minutes)
    # if len(str(hours)) == 1:
    #   hours = '0' + str(hours)

    # final = f"{hours}:{minutes}:{seconds}"
  return final


# Simplified solution

# def make_readable(input):
#   if input > 356399:
#     return "99:59:59"
  
#   hours = input // 3600
#   minutes = (input % 3600) // 60
#   seconds = input % 60

#   formatted = f"{hours:02}:{minutes:02}:{seconds:02}"
#   return formatted

print(make_readable(0)) # Should return '00:00:00'
print(make_readable(15)) # Should return '00:00:15'
print(make_readable(111000)) # Should return '30:50:00'
print(make_readable(356400)) # Should return max value