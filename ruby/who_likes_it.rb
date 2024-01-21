# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"


def likes(names)
  if names.length == 0
    "no one likes this"
  elsif names.length == 1
    "#{names[0]} likes this"
  elsif names.length == 2
    "#{names[0]} and #{names[1]} like this"
  elsif names.length == 3
    "#{names[0]}, #{names[1]} and #{names[2]} like this"
  elsif names.length >= 4
    "#{names[0]}, #{names[1]} and #{(names.length - 2)} others like this"
  end
end

## Alternate solution using 'when' cases
# def likes(names)
#   case names.size
#   when 0 
#     "no one likes this"
#   when 1 
#     "#{names[0]} likes this"
#   when 2
#     "#{names[0]} and #{names[1]} like this"
#   when 3
#     "#{names[0]}, #{names[1]} and #{names[2]} like this"
#   else
#     "#{names[0]}, #{names[1]} and #{names.size - 2} others like this"
#   end
# end

p likes([])
p likes(["Peter"])
p likes(["Jacob", "Alex"])
p likes(["Max", "John", "Mark"])
p likes(["Alex", "Jacob", "Mark", "Max"])
