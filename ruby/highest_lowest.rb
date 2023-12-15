# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

# Examples
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"

# Notes
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.


def high_and_low(numbers)
  array = numbers.split
  nums = array.map do |num|
    num.to_i
  end
  
  sorted = nums.sort

  ## first attempt
  # high = nums[0]
  # low = nums[0]
  # nums.each do |num|
  #   if num > high
  #     high = num
  #   elsif num < low
  #     low = num
  #   end
  # end
  
  return "#{sorted.last} #{sorted.first}"
end

p high_and_low("-2 -1 0 1 2 3 4 5")
p high_and_low("-5 -4 -3 -2 -1 0 1 2 3 4 5")
p high_and_low("0 1 2 3 4 5 6 7 8 9 10")