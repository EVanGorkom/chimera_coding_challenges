array_nums = [
    [1, 2, 3], 
    [8, 9, 4], 
    [7, 6, 5]
  ]

# expect = [1, 2, 3, 4, 5, 6, 7, 8, 9]

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
  # I need a loop in case the array is very large
  
  final_array 
end

p snail(array_nums)