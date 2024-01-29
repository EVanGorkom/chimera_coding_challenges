# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# Examples (input --> output):
# 255, 255, 255 --> "FFFFFF"
# 255, 255, 300 --> "FFFFFF"
# 0, 0, 0       --> "000000"
# 148, 0, 211   --> "9400D3"
import pdb
import math

def rgb(r, g, b):
  # result = ''

  r = max(0, min(r, 255))
  g = max(0, min(g, 255))
  b = max(0, min(b, 255))

  hexadecimal = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B',12: 'C', 13: 'D', 14: 'E', 15: 'F'
    }
  
  r1 = hexadecimal[r // 16]
  r2 = hexadecimal[r % 16]

  g1 = hexadecimal[g // 16]
  g2 = hexadecimal[g % 16]

  b1 = hexadecimal[b // 16]
  b2 = hexadecimal[b % 16]

  # result += (r1 + r2 + g1 + g2 + b1 + b2)
  # return result
  return (r1 + r2 + g1 + g2 + b1 + b2)


print(rgb(255, 255, 255))   # "FFFFFF"
print(rgb(255, 255, 300))   # "FFFFFF" (300 is rounded to 255)
print(rgb(0, 0, 0))         # "000000"
print(rgb(148, 0, 211))     # "9400D3"
