# Instructions
# Create a method/function that will intake a set of brackets [ { ( as a string and determine if the brackets are well-formed (match). Brackets can be nested.

#     bracket('{}')
#     // => true

#     bracket('{()}')
#     // => true

#     bracket('({[]}{[]})') 
#     // => true
    
#     bracket('{(')
#     // => false
    
#     bracket('{[)][]}')
#     // => false
    
#     bracket(']')
#     // => false


def bracket(input)
  # cut the input in half. If it's odd, return false automatically.
  # Once in half, iterate through the index values. 
    # If the value of position 0 is NOT equal to the opposite bracket value, then break the loop and return false.
    # else continue iterating and return True if finished.

    # The big question. How do I equate the values? I would need to hard code the possible reflections.
      # if '(' then ')' is opposite type situation. for each bracket type.
  opposites = {
    '(' => ')',
    '{' => '}',
    '[' => ']',
    '<' => '>',
    ')' => '(',
    '}' => '{',
    ']' => '[',
    '>' => '<'
  }

  if input.length.odd?
    return false
  end

  input_array = input.chars

  if input_array.length == 2
    first_half = input_array[0]
    return opposites[first_half] == input_array[1] ? true : false
  else
    first_half = input_array[0..(input_array.length / 2 - 1)]
    second_half = input_array[(input_array.length / 2)..-1].reverse

    second_half_start_index = 0
    first_half.each do |element|
      if opposites[element] != second_half[second_half_start_index]
        return false
      else 
        second_half_start_index += 1
      end
      return true
    end
  end
end

p bracket('{}') # Should return True
p bracket('{([])}') # Should return True
p bracket('{[]))') # Should return False
p bracket(')') # Should return False
p bracket('{[]))]') # Should return False

p bracket('}}{{') # Should return True