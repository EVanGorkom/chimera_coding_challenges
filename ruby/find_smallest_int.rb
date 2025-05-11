# Given an array of integers your solution should find the smallest integer.

# For example:
# Given [34, 15, 88, 2] your solution will return 2
# Given [34, -345, -1, 100] your solution will return -345
# You can assume, for the purpose of this kata, that the supplied array will not be empty.

def find_smallest_int(arr)
  # arr.min()
  # This is a little too easy with the built-in functions so here's the answer without it.

  smallest_num = arr[0]

  for num in arr
    if num < smallest_num
      smallest_num = num
    end
  end

  return smallest_num
end

array = [34, 15, 88, 2]
puts(find_smallest_int(array))

array = [34, -345, -1, 100]
puts(find_smallest_int(array))
