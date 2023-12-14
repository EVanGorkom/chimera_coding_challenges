array_nums = [
    [0, 7, 8], 
    [9, 3, 4], 
    [5, 1, 11]
  ]

# expect = [ 0 7 8 4 11 1 5 9 3]

def snail(array)
  final_array = []

  array[0].each do |index|
    final_array << index
  end

  array[1..-1].each do |index|
    final_array << index[-1]
  end

  temp = array[-1].reverse

  temp.each do |index|
    final_array << index
  end
  
  require 'pry';binding.pry
  final_array 
end

snail(array_nums)