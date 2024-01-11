# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# moveZeros [1,2,0,1,0,1,0,3,0,1] #-> [1,2,1,1,3,1,0,0,0,0]

def move_zeros(arr) 
  nums = arr.select { |num| num != 0 }
  zeros = arr.select { |num| num == 0 }
  return nums + zeros
end

a = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9]
p move_zeros(a)
# p move_zeros(b)