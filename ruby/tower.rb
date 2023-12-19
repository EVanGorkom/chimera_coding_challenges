# Build Tower
# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

# For example, a tower with 3 floors looks like this:

# [
#   "  *  ",
#   " *** ", 
#   "*****"
# ]
# And a tower with 6 floors looks like this:

# [
#   "     *     ", 
#   "    ***    ", 
#   "   *****   ", 
#   "  *******  ", 
#   " ********* ", 
#   "***********"
# ]

def towerBuilder(n_floors)
  tower_array = []
  counter = 1

  n_floors.times do 
    floor_string = ""
    counter.times do
      floor_string << "*"
    end
    tower_array << floor_string
    counter += 2
  end

  new_array = tower_array.map do |floor|
    diff = tower_array[-1].length - floor.length
    (diff / 2).times do
      floor = " " + floor + " "
    end
    floor
  end
end

p towerBuilder(3)
p towerBuilder(5)
p towerBuilder(6)

# # Simplified answer:
# def towerBuilder(n)
#   (1..n).map do |i|
#     space = ' ' * (n - i)
#     stars = '*' * (i * 2 - 1)
#     space + stars + space
#   end
# end