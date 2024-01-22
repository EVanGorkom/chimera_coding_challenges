# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)
# [160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)

# def find_outlier(integers)
#   odd_nums = 0
#   even_nums = 0

#   integers[0..2].each do |num|
#     if num.odd?
#       odd_nums += 1
#     elsif num.even?
#       even_nums += 1
#     end
#   end

#   if odd_nums > even_nums
#     integers.each do |num|
#       if num.even?
#         return num
#       end
#     end

#   else 
#     integers.each do |num|
#       if num.odd?
#         return num
#       end
#     end
#   end
# end

## Refactored//Simplified solution
def find_outlier(integers)
  even_count = integers.count(&:even?)
  odd_count = integers.count(&:odd?)

  if even_count > odd_count 
    integers.find(&:odd?)
  else 
    integers.find(&:even?)
  end
end

p find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])
p find_outlier([160, 3, 1719, 19, 11, 13, -21])